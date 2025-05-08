"""
Type annotations for omics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_omics.type_defs import AbortMultipartReadSetUploadRequestTypeDef

    data: AbortMultipartReadSetUploadRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AnnotationTypeType,
    CacheBehaviorType,
    CreationTypeType,
    ETagAlgorithmFamilyType,
    ETagAlgorithmType,
    FileTypeType,
    FormatToHeaderKeyType,
    JobStatusType,
    ReadSetActivationJobItemStatusType,
    ReadSetActivationJobStatusType,
    ReadSetExportJobItemStatusType,
    ReadSetExportJobStatusType,
    ReadSetFileType,
    ReadSetImportJobItemStatusType,
    ReadSetImportJobStatusType,
    ReadSetPartSourceType,
    ReadSetStatusType,
    ReferenceFileType,
    ReferenceImportJobItemStatusType,
    ReferenceImportJobStatusType,
    ReferenceStatusType,
    ResourceOwnerType,
    RunCacheStatusType,
    RunLogLevelType,
    RunRetentionModeType,
    RunStatusType,
    SchemaValueTypeType,
    SequenceStoreStatusType,
    ShareResourceTypeType,
    ShareStatusType,
    StorageTypeType,
    StoreFormatType,
    StoreStatusType,
    StoreTypeType,
    TaskStatusType,
    VersionStatusType,
    WorkflowEngineType,
    WorkflowStatusType,
    WorkflowTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AbortMultipartReadSetUploadRequestTypeDef",
    "AcceptShareRequestTypeDef",
    "AcceptShareResponseTypeDef",
    "ActivateReadSetFilterTypeDef",
    "ActivateReadSetJobItemTypeDef",
    "ActivateReadSetSourceItemTypeDef",
    "AnnotationImportItemDetailTypeDef",
    "AnnotationImportItemSourceTypeDef",
    "AnnotationImportJobItemTypeDef",
    "AnnotationStoreItemTypeDef",
    "AnnotationStoreVersionItemTypeDef",
    "BatchDeleteReadSetRequestTypeDef",
    "BatchDeleteReadSetResponseTypeDef",
    "BlobTypeDef",
    "CancelAnnotationImportRequestTypeDef",
    "CancelRunRequestTypeDef",
    "CancelVariantImportRequestTypeDef",
    "CompleteMultipartReadSetUploadRequestTypeDef",
    "CompleteMultipartReadSetUploadResponseTypeDef",
    "CompleteReadSetUploadPartListItemTypeDef",
    "CreateAnnotationStoreRequestTypeDef",
    "CreateAnnotationStoreResponseTypeDef",
    "CreateAnnotationStoreVersionRequestTypeDef",
    "CreateAnnotationStoreVersionResponseTypeDef",
    "CreateMultipartReadSetUploadRequestTypeDef",
    "CreateMultipartReadSetUploadResponseTypeDef",
    "CreateReferenceStoreRequestTypeDef",
    "CreateReferenceStoreResponseTypeDef",
    "CreateRunCacheRequestTypeDef",
    "CreateRunCacheResponseTypeDef",
    "CreateRunGroupRequestTypeDef",
    "CreateRunGroupResponseTypeDef",
    "CreateSequenceStoreRequestTypeDef",
    "CreateSequenceStoreResponseTypeDef",
    "CreateShareRequestTypeDef",
    "CreateShareResponseTypeDef",
    "CreateVariantStoreRequestTypeDef",
    "CreateVariantStoreResponseTypeDef",
    "CreateWorkflowRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateWorkflowVersionRequestTypeDef",
    "CreateWorkflowVersionResponseTypeDef",
    "DeleteAnnotationStoreRequestTypeDef",
    "DeleteAnnotationStoreResponseTypeDef",
    "DeleteAnnotationStoreVersionsRequestTypeDef",
    "DeleteAnnotationStoreVersionsResponseTypeDef",
    "DeleteReferenceRequestTypeDef",
    "DeleteReferenceStoreRequestTypeDef",
    "DeleteRunCacheRequestTypeDef",
    "DeleteRunGroupRequestTypeDef",
    "DeleteRunRequestTypeDef",
    "DeleteS3AccessPolicyRequestTypeDef",
    "DeleteSequenceStoreRequestTypeDef",
    "DeleteShareRequestTypeDef",
    "DeleteShareResponseTypeDef",
    "DeleteVariantStoreRequestTypeDef",
    "DeleteVariantStoreResponseTypeDef",
    "DeleteWorkflowRequestTypeDef",
    "DeleteWorkflowVersionRequestTypeDef",
    "ETagTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportReadSetDetailTypeDef",
    "ExportReadSetFilterTypeDef",
    "ExportReadSetJobDetailTypeDef",
    "ExportReadSetTypeDef",
    "FileInformationTypeDef",
    "FilterTypeDef",
    "FormatOptionsTypeDef",
    "GetAnnotationImportRequestTypeDef",
    "GetAnnotationImportRequestWaitTypeDef",
    "GetAnnotationImportResponseTypeDef",
    "GetAnnotationStoreRequestTypeDef",
    "GetAnnotationStoreRequestWaitExtraTypeDef",
    "GetAnnotationStoreRequestWaitTypeDef",
    "GetAnnotationStoreResponseTypeDef",
    "GetAnnotationStoreVersionRequestTypeDef",
    "GetAnnotationStoreVersionRequestWaitExtraTypeDef",
    "GetAnnotationStoreVersionRequestWaitTypeDef",
    "GetAnnotationStoreVersionResponseTypeDef",
    "GetReadSetActivationJobRequestTypeDef",
    "GetReadSetActivationJobRequestWaitTypeDef",
    "GetReadSetActivationJobResponseTypeDef",
    "GetReadSetExportJobRequestTypeDef",
    "GetReadSetExportJobRequestWaitTypeDef",
    "GetReadSetExportJobResponseTypeDef",
    "GetReadSetImportJobRequestTypeDef",
    "GetReadSetImportJobRequestWaitTypeDef",
    "GetReadSetImportJobResponseTypeDef",
    "GetReadSetMetadataRequestTypeDef",
    "GetReadSetMetadataResponseTypeDef",
    "GetReadSetRequestTypeDef",
    "GetReadSetResponseTypeDef",
    "GetReferenceImportJobRequestTypeDef",
    "GetReferenceImportJobRequestWaitTypeDef",
    "GetReferenceImportJobResponseTypeDef",
    "GetReferenceMetadataRequestTypeDef",
    "GetReferenceMetadataResponseTypeDef",
    "GetReferenceRequestTypeDef",
    "GetReferenceResponseTypeDef",
    "GetReferenceStoreRequestTypeDef",
    "GetReferenceStoreResponseTypeDef",
    "GetRunCacheRequestTypeDef",
    "GetRunCacheResponseTypeDef",
    "GetRunGroupRequestTypeDef",
    "GetRunGroupResponseTypeDef",
    "GetRunRequestTypeDef",
    "GetRunRequestWaitExtraTypeDef",
    "GetRunRequestWaitTypeDef",
    "GetRunResponseTypeDef",
    "GetRunTaskRequestTypeDef",
    "GetRunTaskRequestWaitExtraTypeDef",
    "GetRunTaskRequestWaitTypeDef",
    "GetRunTaskResponseTypeDef",
    "GetS3AccessPolicyRequestTypeDef",
    "GetS3AccessPolicyResponseTypeDef",
    "GetSequenceStoreRequestTypeDef",
    "GetSequenceStoreResponseTypeDef",
    "GetShareRequestTypeDef",
    "GetShareResponseTypeDef",
    "GetVariantImportRequestTypeDef",
    "GetVariantImportRequestWaitTypeDef",
    "GetVariantImportResponseTypeDef",
    "GetVariantStoreRequestTypeDef",
    "GetVariantStoreRequestWaitExtraTypeDef",
    "GetVariantStoreRequestWaitTypeDef",
    "GetVariantStoreResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowRequestWaitTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowVersionRequestTypeDef",
    "GetWorkflowVersionRequestWaitTypeDef",
    "GetWorkflowVersionResponseTypeDef",
    "ImportReadSetFilterTypeDef",
    "ImportReadSetJobItemTypeDef",
    "ImportReadSetSourceItemTypeDef",
    "ImportReferenceFilterTypeDef",
    "ImportReferenceJobItemTypeDef",
    "ImportReferenceSourceItemTypeDef",
    "ListAnnotationImportJobsFilterTypeDef",
    "ListAnnotationImportJobsRequestPaginateTypeDef",
    "ListAnnotationImportJobsRequestTypeDef",
    "ListAnnotationImportJobsResponseTypeDef",
    "ListAnnotationStoreVersionsFilterTypeDef",
    "ListAnnotationStoreVersionsRequestPaginateTypeDef",
    "ListAnnotationStoreVersionsRequestTypeDef",
    "ListAnnotationStoreVersionsResponseTypeDef",
    "ListAnnotationStoresFilterTypeDef",
    "ListAnnotationStoresRequestPaginateTypeDef",
    "ListAnnotationStoresRequestTypeDef",
    "ListAnnotationStoresResponseTypeDef",
    "ListMultipartReadSetUploadsRequestPaginateTypeDef",
    "ListMultipartReadSetUploadsRequestTypeDef",
    "ListMultipartReadSetUploadsResponseTypeDef",
    "ListReadSetActivationJobsRequestPaginateTypeDef",
    "ListReadSetActivationJobsRequestTypeDef",
    "ListReadSetActivationJobsResponseTypeDef",
    "ListReadSetExportJobsRequestPaginateTypeDef",
    "ListReadSetExportJobsRequestTypeDef",
    "ListReadSetExportJobsResponseTypeDef",
    "ListReadSetImportJobsRequestPaginateTypeDef",
    "ListReadSetImportJobsRequestTypeDef",
    "ListReadSetImportJobsResponseTypeDef",
    "ListReadSetUploadPartsRequestPaginateTypeDef",
    "ListReadSetUploadPartsRequestTypeDef",
    "ListReadSetUploadPartsResponseTypeDef",
    "ListReadSetsRequestPaginateTypeDef",
    "ListReadSetsRequestTypeDef",
    "ListReadSetsResponseTypeDef",
    "ListReferenceImportJobsRequestPaginateTypeDef",
    "ListReferenceImportJobsRequestTypeDef",
    "ListReferenceImportJobsResponseTypeDef",
    "ListReferenceStoresRequestPaginateTypeDef",
    "ListReferenceStoresRequestTypeDef",
    "ListReferenceStoresResponseTypeDef",
    "ListReferencesRequestPaginateTypeDef",
    "ListReferencesRequestTypeDef",
    "ListReferencesResponseTypeDef",
    "ListRunCachesRequestPaginateTypeDef",
    "ListRunCachesRequestTypeDef",
    "ListRunCachesResponseTypeDef",
    "ListRunGroupsRequestPaginateTypeDef",
    "ListRunGroupsRequestTypeDef",
    "ListRunGroupsResponseTypeDef",
    "ListRunTasksRequestPaginateTypeDef",
    "ListRunTasksRequestTypeDef",
    "ListRunTasksResponseTypeDef",
    "ListRunsRequestPaginateTypeDef",
    "ListRunsRequestTypeDef",
    "ListRunsResponseTypeDef",
    "ListSequenceStoresRequestPaginateTypeDef",
    "ListSequenceStoresRequestTypeDef",
    "ListSequenceStoresResponseTypeDef",
    "ListSharesRequestPaginateTypeDef",
    "ListSharesRequestTypeDef",
    "ListSharesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVariantImportJobsFilterTypeDef",
    "ListVariantImportJobsRequestPaginateTypeDef",
    "ListVariantImportJobsRequestTypeDef",
    "ListVariantImportJobsResponseTypeDef",
    "ListVariantStoresFilterTypeDef",
    "ListVariantStoresRequestPaginateTypeDef",
    "ListVariantStoresRequestTypeDef",
    "ListVariantStoresResponseTypeDef",
    "ListWorkflowVersionsRequestPaginateTypeDef",
    "ListWorkflowVersionsRequestTypeDef",
    "ListWorkflowVersionsResponseTypeDef",
    "ListWorkflowsRequestPaginateTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MultipartReadSetUploadListItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutS3AccessPolicyRequestTypeDef",
    "PutS3AccessPolicyResponseTypeDef",
    "ReadOptionsTypeDef",
    "ReadSetBatchErrorTypeDef",
    "ReadSetFilesTypeDef",
    "ReadSetFilterTypeDef",
    "ReadSetListItemTypeDef",
    "ReadSetS3AccessTypeDef",
    "ReadSetUploadPartListFilterTypeDef",
    "ReadSetUploadPartListItemTypeDef",
    "ReferenceFilesTypeDef",
    "ReferenceFilterTypeDef",
    "ReferenceItemTypeDef",
    "ReferenceListItemTypeDef",
    "ReferenceStoreDetailTypeDef",
    "ReferenceStoreFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RunCacheListItemTypeDef",
    "RunGroupListItemTypeDef",
    "RunListItemTypeDef",
    "RunLogLocationTypeDef",
    "S3AccessConfigTypeDef",
    "SequenceInformationTypeDef",
    "SequenceStoreDetailTypeDef",
    "SequenceStoreFilterTypeDef",
    "SequenceStoreS3AccessTypeDef",
    "ShareDetailsTypeDef",
    "SourceFilesTypeDef",
    "SseConfigTypeDef",
    "StartAnnotationImportRequestTypeDef",
    "StartAnnotationImportResponseTypeDef",
    "StartReadSetActivationJobRequestTypeDef",
    "StartReadSetActivationJobResponseTypeDef",
    "StartReadSetActivationJobSourceItemTypeDef",
    "StartReadSetExportJobRequestTypeDef",
    "StartReadSetExportJobResponseTypeDef",
    "StartReadSetImportJobRequestTypeDef",
    "StartReadSetImportJobResponseTypeDef",
    "StartReadSetImportJobSourceItemTypeDef",
    "StartReferenceImportJobRequestTypeDef",
    "StartReferenceImportJobResponseTypeDef",
    "StartReferenceImportJobSourceItemTypeDef",
    "StartRunRequestTypeDef",
    "StartRunResponseTypeDef",
    "StartVariantImportRequestTypeDef",
    "StartVariantImportResponseTypeDef",
    "StoreOptionsOutputTypeDef",
    "StoreOptionsTypeDef",
    "StoreOptionsUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TaskListItemTypeDef",
    "TimestampTypeDef",
    "TsvOptionsTypeDef",
    "TsvStoreOptionsOutputTypeDef",
    "TsvStoreOptionsTypeDef",
    "TsvVersionOptionsOutputTypeDef",
    "TsvVersionOptionsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAnnotationStoreRequestTypeDef",
    "UpdateAnnotationStoreResponseTypeDef",
    "UpdateAnnotationStoreVersionRequestTypeDef",
    "UpdateAnnotationStoreVersionResponseTypeDef",
    "UpdateRunCacheRequestTypeDef",
    "UpdateRunGroupRequestTypeDef",
    "UpdateSequenceStoreRequestTypeDef",
    "UpdateSequenceStoreResponseTypeDef",
    "UpdateVariantStoreRequestTypeDef",
    "UpdateVariantStoreResponseTypeDef",
    "UpdateWorkflowRequestTypeDef",
    "UpdateWorkflowVersionRequestTypeDef",
    "UploadReadSetPartRequestTypeDef",
    "UploadReadSetPartResponseTypeDef",
    "VariantImportItemDetailTypeDef",
    "VariantImportItemSourceTypeDef",
    "VariantImportJobItemTypeDef",
    "VariantStoreItemTypeDef",
    "VcfOptionsTypeDef",
    "VersionDeleteErrorTypeDef",
    "VersionOptionsOutputTypeDef",
    "VersionOptionsTypeDef",
    "VersionOptionsUnionTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowListItemTypeDef",
    "WorkflowParameterTypeDef",
    "WorkflowVersionListItemTypeDef",
)

class AbortMultipartReadSetUploadRequestTypeDef(TypedDict):
    sequenceStoreId: str
    uploadId: str

class AcceptShareRequestTypeDef(TypedDict):
    shareId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]
ActivateReadSetJobItemTypeDef = TypedDict(
    "ActivateReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)

class ActivateReadSetSourceItemTypeDef(TypedDict):
    readSetId: str
    status: ReadSetActivationJobItemStatusType
    statusMessage: NotRequired[str]

class AnnotationImportItemDetailTypeDef(TypedDict):
    source: str
    jobStatus: JobStatusType

class AnnotationImportItemSourceTypeDef(TypedDict):
    source: str

AnnotationImportJobItemTypeDef = TypedDict(
    "AnnotationImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "versionName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": NotRequired[datetime],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Dict[str, str]],
    },
)

class ReferenceItemTypeDef(TypedDict):
    referenceArn: NotRequired[str]

SseConfigTypeDef = TypedDict(
    "SseConfigTypeDef",
    {
        "type": Literal["KMS"],
        "keyArn": NotRequired[str],
    },
)
AnnotationStoreVersionItemTypeDef = TypedDict(
    "AnnotationStoreVersionItemTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "versionArn": str,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "versionSizeBytes": int,
    },
)

class BatchDeleteReadSetRequestTypeDef(TypedDict):
    ids: Sequence[str]
    sequenceStoreId: str

ReadSetBatchErrorTypeDef = TypedDict(
    "ReadSetBatchErrorTypeDef",
    {
        "id": str,
        "code": str,
        "message": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelAnnotationImportRequestTypeDef(TypedDict):
    jobId: str

CancelRunRequestTypeDef = TypedDict(
    "CancelRunRequestTypeDef",
    {
        "id": str,
    },
)

class CancelVariantImportRequestTypeDef(TypedDict):
    jobId: str

class CompleteReadSetUploadPartListItemTypeDef(TypedDict):
    partNumber: int
    partSource: ReadSetPartSourceType
    checksum: str

class CreateMultipartReadSetUploadRequestTypeDef(TypedDict):
    sequenceStoreId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    name: str
    clientToken: NotRequired[str]
    generatedFrom: NotRequired[str]
    referenceArn: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateRunCacheRequestTypeDef(TypedDict):
    cacheS3Location: str
    requestId: str
    cacheBehavior: NotRequired[CacheBehaviorType]
    description: NotRequired[str]
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    cacheBucketOwnerId: NotRequired[str]

class CreateRunGroupRequestTypeDef(TypedDict):
    requestId: str
    name: NotRequired[str]
    maxCpus: NotRequired[int]
    maxRuns: NotRequired[int]
    maxDuration: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    maxGpus: NotRequired[int]

class S3AccessConfigTypeDef(TypedDict):
    accessLogLocation: NotRequired[str]

class SequenceStoreS3AccessTypeDef(TypedDict):
    s3Uri: NotRequired[str]
    s3AccessPointArn: NotRequired[str]
    accessLogLocation: NotRequired[str]

class CreateShareRequestTypeDef(TypedDict):
    resourceArn: str
    principalSubscriber: str
    shareName: NotRequired[str]

class WorkflowParameterTypeDef(TypedDict):
    description: NotRequired[str]
    optional: NotRequired[bool]

class DeleteAnnotationStoreRequestTypeDef(TypedDict):
    name: str
    force: NotRequired[bool]

class DeleteAnnotationStoreVersionsRequestTypeDef(TypedDict):
    name: str
    versions: Sequence[str]
    force: NotRequired[bool]

class VersionDeleteErrorTypeDef(TypedDict):
    versionName: str
    message: str

DeleteReferenceRequestTypeDef = TypedDict(
    "DeleteReferenceRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)
DeleteReferenceStoreRequestTypeDef = TypedDict(
    "DeleteReferenceStoreRequestTypeDef",
    {
        "id": str,
    },
)
DeleteRunCacheRequestTypeDef = TypedDict(
    "DeleteRunCacheRequestTypeDef",
    {
        "id": str,
    },
)
DeleteRunGroupRequestTypeDef = TypedDict(
    "DeleteRunGroupRequestTypeDef",
    {
        "id": str,
    },
)
DeleteRunRequestTypeDef = TypedDict(
    "DeleteRunRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteS3AccessPolicyRequestTypeDef(TypedDict):
    s3AccessPointArn: str

DeleteSequenceStoreRequestTypeDef = TypedDict(
    "DeleteSequenceStoreRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteShareRequestTypeDef(TypedDict):
    shareId: str

class DeleteVariantStoreRequestTypeDef(TypedDict):
    name: str
    force: NotRequired[bool]

DeleteWorkflowRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteWorkflowVersionRequestTypeDef(TypedDict):
    workflowId: str
    versionName: str

class ETagTypeDef(TypedDict):
    algorithm: NotRequired[ETagAlgorithmType]
    source1: NotRequired[str]
    source2: NotRequired[str]

ExportReadSetDetailTypeDef = TypedDict(
    "ExportReadSetDetailTypeDef",
    {
        "id": str,
        "status": ReadSetExportJobItemStatusType,
        "statusMessage": NotRequired[str],
    },
)
ExportReadSetJobDetailTypeDef = TypedDict(
    "ExportReadSetJobDetailTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)

class ExportReadSetTypeDef(TypedDict):
    readSetId: str

class ReadSetS3AccessTypeDef(TypedDict):
    s3Uri: NotRequired[str]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "resourceArns": NotRequired[Sequence[str]],
        "status": NotRequired[Sequence[ShareStatusType]],
        "type": NotRequired[Sequence[ShareResourceTypeType]],
    },
)

class VcfOptionsTypeDef(TypedDict):
    ignoreQualField: NotRequired[bool]
    ignoreFilterField: NotRequired[bool]

class GetAnnotationImportRequestTypeDef(TypedDict):
    jobId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetAnnotationStoreRequestTypeDef(TypedDict):
    name: str

class GetAnnotationStoreVersionRequestTypeDef(TypedDict):
    name: str
    versionName: str

GetReadSetActivationJobRequestTypeDef = TypedDict(
    "GetReadSetActivationJobRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)
GetReadSetExportJobRequestTypeDef = TypedDict(
    "GetReadSetExportJobRequestTypeDef",
    {
        "sequenceStoreId": str,
        "id": str,
    },
)
GetReadSetImportJobRequestTypeDef = TypedDict(
    "GetReadSetImportJobRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)
GetReadSetMetadataRequestTypeDef = TypedDict(
    "GetReadSetMetadataRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)

class SequenceInformationTypeDef(TypedDict):
    totalReadCount: NotRequired[int]
    totalBaseCount: NotRequired[int]
    generatedFrom: NotRequired[str]
    alignment: NotRequired[str]

GetReadSetRequestTypeDef = TypedDict(
    "GetReadSetRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "partNumber": int,
        "file": NotRequired[ReadSetFileType],
    },
)
GetReferenceImportJobRequestTypeDef = TypedDict(
    "GetReferenceImportJobRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)

class ImportReferenceSourceItemTypeDef(TypedDict):
    status: ReferenceImportJobItemStatusType
    sourceFile: NotRequired[str]
    statusMessage: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    referenceId: NotRequired[str]

GetReferenceMetadataRequestTypeDef = TypedDict(
    "GetReferenceMetadataRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)
GetReferenceRequestTypeDef = TypedDict(
    "GetReferenceRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "partNumber": int,
        "range": NotRequired[str],
        "file": NotRequired[ReferenceFileType],
    },
)
GetReferenceStoreRequestTypeDef = TypedDict(
    "GetReferenceStoreRequestTypeDef",
    {
        "id": str,
    },
)
GetRunCacheRequestTypeDef = TypedDict(
    "GetRunCacheRequestTypeDef",
    {
        "id": str,
    },
)
GetRunGroupRequestTypeDef = TypedDict(
    "GetRunGroupRequestTypeDef",
    {
        "id": str,
    },
)
GetRunRequestTypeDef = TypedDict(
    "GetRunRequestTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
    },
)

class RunLogLocationTypeDef(TypedDict):
    engineLogStream: NotRequired[str]
    runLogStream: NotRequired[str]

GetRunTaskRequestTypeDef = TypedDict(
    "GetRunTaskRequestTypeDef",
    {
        "id": str,
        "taskId": str,
    },
)

class GetS3AccessPolicyRequestTypeDef(TypedDict):
    s3AccessPointArn: str

GetSequenceStoreRequestTypeDef = TypedDict(
    "GetSequenceStoreRequestTypeDef",
    {
        "id": str,
    },
)

class GetShareRequestTypeDef(TypedDict):
    shareId: str

class ShareDetailsTypeDef(TypedDict):
    shareId: NotRequired[str]
    resourceArn: NotRequired[str]
    resourceId: NotRequired[str]
    principalSubscriber: NotRequired[str]
    ownerId: NotRequired[str]
    status: NotRequired[ShareStatusType]
    statusMessage: NotRequired[str]
    shareName: NotRequired[str]
    creationTime: NotRequired[datetime]
    updateTime: NotRequired[datetime]

class GetVariantImportRequestTypeDef(TypedDict):
    jobId: str

class VariantImportItemDetailTypeDef(TypedDict):
    source: str
    jobStatus: JobStatusType
    statusMessage: NotRequired[str]

class GetVariantStoreRequestTypeDef(TypedDict):
    name: str

GetWorkflowRequestTypeDef = TypedDict(
    "GetWorkflowRequestTypeDef",
    {
        "id": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
    },
)
GetWorkflowVersionRequestTypeDef = TypedDict(
    "GetWorkflowVersionRequestTypeDef",
    {
        "workflowId": str,
        "versionName": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
    },
)
ImportReadSetJobItemTypeDef = TypedDict(
    "ImportReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)

class SourceFilesTypeDef(TypedDict):
    source1: str
    source2: NotRequired[str]

ImportReferenceJobItemTypeDef = TypedDict(
    "ImportReferenceJobItemTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)

class ListAnnotationImportJobsFilterTypeDef(TypedDict):
    status: NotRequired[JobStatusType]
    storeName: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAnnotationStoreVersionsFilterTypeDef(TypedDict):
    status: NotRequired[VersionStatusType]

class ListAnnotationStoresFilterTypeDef(TypedDict):
    status: NotRequired[StoreStatusType]

class ListMultipartReadSetUploadsRequestTypeDef(TypedDict):
    sequenceStoreId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class MultipartReadSetUploadListItemTypeDef(TypedDict):
    sequenceStoreId: str
    uploadId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: str
    referenceArn: str
    creationTime: datetime
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ReadSetUploadPartListItemTypeDef(TypedDict):
    partNumber: int
    partSize: int
    partSource: ReadSetPartSourceType
    checksum: str
    creationTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]

ReferenceListItemTypeDef = TypedDict(
    "ReferenceListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "referenceStoreId": str,
        "md5": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "status": NotRequired[ReferenceStatusType],
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)

class ListRunCachesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    startingToken: NotRequired[str]

RunCacheListItemTypeDef = TypedDict(
    "RunCacheListItemTypeDef",
    {
        "arn": NotRequired[str],
        "cacheBehavior": NotRequired[CacheBehaviorType],
        "cacheS3Uri": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[RunCacheStatusType],
    },
)

class ListRunGroupsRequestTypeDef(TypedDict):
    name: NotRequired[str]
    startingToken: NotRequired[str]
    maxResults: NotRequired[int]

RunGroupListItemTypeDef = TypedDict(
    "RunGroupListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "maxCpus": NotRequired[int],
        "maxRuns": NotRequired[int],
        "maxDuration": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "maxGpus": NotRequired[int],
    },
)
ListRunTasksRequestTypeDef = TypedDict(
    "ListRunTasksRequestTypeDef",
    {
        "id": str,
        "status": NotRequired[TaskStatusType],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class TaskListItemTypeDef(TypedDict):
    taskId: NotRequired[str]
    status: NotRequired[TaskStatusType]
    name: NotRequired[str]
    cpus: NotRequired[int]
    cacheHit: NotRequired[bool]
    cacheS3Uri: NotRequired[str]
    memory: NotRequired[int]
    creationTime: NotRequired[datetime]
    startTime: NotRequired[datetime]
    stopTime: NotRequired[datetime]
    gpus: NotRequired[int]
    instanceType: NotRequired[str]

class ListRunsRequestTypeDef(TypedDict):
    name: NotRequired[str]
    runGroupId: NotRequired[str]
    startingToken: NotRequired[str]
    maxResults: NotRequired[int]
    status: NotRequired[RunStatusType]

RunListItemTypeDef = TypedDict(
    "RunListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[RunStatusType],
        "workflowId": NotRequired[str],
        "name": NotRequired[str],
        "priority": NotRequired[int],
        "storageCapacity": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "stopTime": NotRequired[datetime],
        "storageType": NotRequired[StorageTypeType],
        "workflowVersionName": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListVariantImportJobsFilterTypeDef(TypedDict):
    status: NotRequired[JobStatusType]
    storeName: NotRequired[str]

VariantImportJobItemTypeDef = TypedDict(
    "VariantImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": NotRequired[datetime],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Dict[str, str]],
    },
)

class ListVariantStoresFilterTypeDef(TypedDict):
    status: NotRequired[StoreStatusType]

ListWorkflowVersionsRequestTypeDef = TypedDict(
    "ListWorkflowVersionsRequestTypeDef",
    {
        "workflowId": str,
        "type": NotRequired[WorkflowTypeType],
        "workflowOwnerId": NotRequired[str],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkflowVersionListItemTypeDef = TypedDict(
    "WorkflowVersionListItemTypeDef",
    {
        "arn": NotRequired[str],
        "workflowId": NotRequired[str],
        "versionName": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[WorkflowStatusType],
        "type": NotRequired[WorkflowTypeType],
        "digest": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "metadata": NotRequired[Dict[str, str]],
    },
)
ListWorkflowsRequestTypeDef = TypedDict(
    "ListWorkflowsRequestTypeDef",
    {
        "type": NotRequired[WorkflowTypeType],
        "name": NotRequired[str],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkflowListItemTypeDef = TypedDict(
    "WorkflowListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[WorkflowStatusType],
        "type": NotRequired[WorkflowTypeType],
        "digest": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "metadata": NotRequired[Dict[str, str]],
    },
)

class PutS3AccessPolicyRequestTypeDef(TypedDict):
    s3AccessPointArn: str
    s3AccessPolicy: str

class ReadOptionsTypeDef(TypedDict):
    sep: NotRequired[str]
    encoding: NotRequired[str]
    quote: NotRequired[str]
    quoteAll: NotRequired[bool]
    escape: NotRequired[str]
    escapeQuotes: NotRequired[bool]
    comment: NotRequired[str]
    header: NotRequired[bool]
    lineSep: NotRequired[str]

class StartReadSetActivationJobSourceItemTypeDef(TypedDict):
    readSetId: str

class StartReferenceImportJobSourceItemTypeDef(TypedDict):
    sourceFile: str
    name: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class StartRunRequestTypeDef(TypedDict):
    roleArn: str
    requestId: str
    workflowId: NotRequired[str]
    workflowType: NotRequired[WorkflowTypeType]
    runId: NotRequired[str]
    name: NotRequired[str]
    cacheId: NotRequired[str]
    cacheBehavior: NotRequired[CacheBehaviorType]
    runGroupId: NotRequired[str]
    priority: NotRequired[int]
    parameters: NotRequired[Mapping[str, Any]]
    storageCapacity: NotRequired[int]
    outputUri: NotRequired[str]
    logLevel: NotRequired[RunLogLevelType]
    tags: NotRequired[Mapping[str, str]]
    retentionMode: NotRequired[RunRetentionModeType]
    storageType: NotRequired[StorageTypeType]
    workflowOwnerId: NotRequired[str]
    workflowVersionName: NotRequired[str]

class VariantImportItemSourceTypeDef(TypedDict):
    source: str

class TsvStoreOptionsOutputTypeDef(TypedDict):
    annotationType: NotRequired[AnnotationTypeType]
    formatToHeader: NotRequired[Dict[FormatToHeaderKeyType, str]]
    schema: NotRequired[List[Dict[str, SchemaValueTypeType]]]

class TsvStoreOptionsTypeDef(TypedDict):
    annotationType: NotRequired[AnnotationTypeType]
    formatToHeader: NotRequired[Mapping[FormatToHeaderKeyType, str]]
    schema: NotRequired[Sequence[Mapping[str, SchemaValueTypeType]]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TsvVersionOptionsOutputTypeDef(TypedDict):
    annotationType: NotRequired[AnnotationTypeType]
    formatToHeader: NotRequired[Dict[FormatToHeaderKeyType, str]]
    schema: NotRequired[List[Dict[str, SchemaValueTypeType]]]

class TsvVersionOptionsTypeDef(TypedDict):
    annotationType: NotRequired[AnnotationTypeType]
    formatToHeader: NotRequired[Mapping[FormatToHeaderKeyType, str]]
    schema: NotRequired[Sequence[Mapping[str, SchemaValueTypeType]]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnnotationStoreRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]

class UpdateAnnotationStoreVersionRequestTypeDef(TypedDict):
    name: str
    versionName: str
    description: NotRequired[str]

UpdateRunCacheRequestTypeDef = TypedDict(
    "UpdateRunCacheRequestTypeDef",
    {
        "id": str,
        "cacheBehavior": NotRequired[CacheBehaviorType],
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
UpdateRunGroupRequestTypeDef = TypedDict(
    "UpdateRunGroupRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "maxCpus": NotRequired[int],
        "maxRuns": NotRequired[int],
        "maxDuration": NotRequired[int],
        "maxGpus": NotRequired[int],
    },
)

class UpdateVariantStoreRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]

UpdateWorkflowRequestTypeDef = TypedDict(
    "UpdateWorkflowRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "storageType": NotRequired[StorageTypeType],
        "storageCapacity": NotRequired[int],
    },
)

class UpdateWorkflowVersionRequestTypeDef(TypedDict):
    workflowId: str
    versionName: str
    description: NotRequired[str]
    storageType: NotRequired[StorageTypeType]
    storageCapacity: NotRequired[int]

class AcceptShareResponseTypeDef(TypedDict):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteMultipartReadSetUploadResponseTypeDef(TypedDict):
    readSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultipartReadSetUploadResponseTypeDef(TypedDict):
    sequenceStoreId: str
    uploadId: str
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: str
    referenceArn: str
    name: str
    description: str
    tags: Dict[str, str]
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

CreateRunCacheResponseTypeDef = TypedDict(
    "CreateRunCacheResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunCacheStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRunGroupResponseTypeDef = TypedDict(
    "CreateRunGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateShareResponseTypeDef(TypedDict):
    shareId: str
    status: ShareStatusType
    shareName: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": WorkflowStatusType,
        "tags": Dict[str, str],
        "uuid": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateWorkflowVersionResponseTypeDef(TypedDict):
    arn: str
    workflowId: str
    versionName: str
    status: WorkflowStatusType
    tags: Dict[str, str]
    uuid: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnnotationStoreResponseTypeDef(TypedDict):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteShareResponseTypeDef(TypedDict):
    status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVariantStoreResponseTypeDef(TypedDict):
    status: StoreStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadSetResponseTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetReferenceResponseTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

GetRunCacheResponseTypeDef = TypedDict(
    "GetRunCacheResponseTypeDef",
    {
        "arn": str,
        "cacheBehavior": CacheBehaviorType,
        "cacheBucketOwnerId": str,
        "cacheS3Uri": str,
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "status": RunCacheStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunGroupResponseTypeDef = TypedDict(
    "GetRunGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "maxCpus": int,
        "maxRuns": int,
        "maxDuration": int,
        "creationTime": datetime,
        "tags": Dict[str, str],
        "maxGpus": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetRunTaskResponseTypeDef(TypedDict):
    taskId: str
    status: TaskStatusType
    name: str
    cpus: int
    cacheHit: bool
    cacheS3Uri: str
    memory: int
    creationTime: datetime
    startTime: datetime
    stopTime: datetime
    statusMessage: str
    logStream: str
    gpus: int
    instanceType: str
    failureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetS3AccessPolicyResponseTypeDef(TypedDict):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    updateTime: datetime
    s3AccessPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutS3AccessPolicyResponseTypeDef(TypedDict):
    s3AccessPointArn: str
    storeId: str
    storeType: StoreTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class StartAnnotationImportResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

StartReadSetActivationJobResponseTypeDef = TypedDict(
    "StartReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetExportJobResponseTypeDef = TypedDict(
    "StartReadSetExportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetImportJobResponseTypeDef = TypedDict(
    "StartReadSetImportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReferenceImportJobResponseTypeDef = TypedDict(
    "StartReferenceImportJobResponseTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRunResponseTypeDef = TypedDict(
    "StartRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunStatusType,
        "tags": Dict[str, str],
        "uuid": str,
        "runOutputUri": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class StartVariantImportResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

UpdateAnnotationStoreVersionResponseTypeDef = TypedDict(
    "UpdateAnnotationStoreVersionResponseTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UploadReadSetPartResponseTypeDef(TypedDict):
    checksum: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateReadSetFilterTypeDef(TypedDict):
    status: NotRequired[ReadSetActivationJobStatusType]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ExportReadSetFilterTypeDef(TypedDict):
    status: NotRequired[ReadSetExportJobStatusType]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ImportReadSetFilterTypeDef(TypedDict):
    status: NotRequired[ReadSetImportJobStatusType]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ImportReferenceFilterTypeDef(TypedDict):
    status: NotRequired[ReferenceImportJobStatusType]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ReadSetFilterTypeDef(TypedDict):
    name: NotRequired[str]
    status: NotRequired[ReadSetStatusType]
    referenceArn: NotRequired[str]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    sampleId: NotRequired[str]
    subjectId: NotRequired[str]
    generatedFrom: NotRequired[str]
    creationType: NotRequired[CreationTypeType]

class ReadSetUploadPartListFilterTypeDef(TypedDict):
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ReferenceFilterTypeDef(TypedDict):
    name: NotRequired[str]
    md5: NotRequired[str]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class ReferenceStoreFilterTypeDef(TypedDict):
    name: NotRequired[str]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]

class SequenceStoreFilterTypeDef(TypedDict):
    name: NotRequired[str]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    status: NotRequired[SequenceStoreStatusType]
    updatedAfter: NotRequired[TimestampTypeDef]
    updatedBefore: NotRequired[TimestampTypeDef]

class ListReadSetActivationJobsResponseTypeDef(TypedDict):
    activationJobs: List[ActivateReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetReadSetActivationJobResponseTypeDef = TypedDict(
    "GetReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ActivateReadSetSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAnnotationImportJobsResponseTypeDef(TypedDict):
    annotationImportJobs: List[AnnotationImportJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateVariantStoreResponseTypeDef = TypedDict(
    "CreateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVariantStoreResponseTypeDef = TypedDict(
    "UpdateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnnotationStoreItemTypeDef = TypedDict(
    "AnnotationStoreItemTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "storeFormat": StoreFormatType,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
    },
)

class CreateReferenceStoreRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    sseConfig: NotRequired[SseConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

CreateReferenceStoreResponseTypeDef = TypedDict(
    "CreateReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateVariantStoreRequestTypeDef(TypedDict):
    reference: ReferenceItemTypeDef
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    sseConfig: NotRequired[SseConfigTypeDef]

GetReferenceStoreResponseTypeDef = TypedDict(
    "GetReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVariantStoreResponseTypeDef = TypedDict(
    "GetVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "statusMessage": str,
        "storeSizeBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReferenceStoreDetailTypeDef = TypedDict(
    "ReferenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
    },
)
SequenceStoreDetailTypeDef = TypedDict(
    "SequenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
        "fallbackLocation": NotRequired[str],
        "eTagAlgorithmFamily": NotRequired[ETagAlgorithmFamilyType],
        "status": NotRequired[SequenceStoreStatusType],
        "statusMessage": NotRequired[str],
        "updateTime": NotRequired[datetime],
    },
)
VariantStoreItemTypeDef = TypedDict(
    "VariantStoreItemTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
    },
)

class ListAnnotationStoreVersionsResponseTypeDef(TypedDict):
    annotationStoreVersions: List[AnnotationStoreVersionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchDeleteReadSetResponseTypeDef(TypedDict):
    errors: List[ReadSetBatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UploadReadSetPartRequestTypeDef(TypedDict):
    sequenceStoreId: str
    uploadId: str
    partSource: ReadSetPartSourceType
    partNumber: int
    payload: BlobTypeDef

class CompleteMultipartReadSetUploadRequestTypeDef(TypedDict):
    sequenceStoreId: str
    uploadId: str
    parts: Sequence[CompleteReadSetUploadPartListItemTypeDef]

class CreateSequenceStoreRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    sseConfig: NotRequired[SseConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    fallbackLocation: NotRequired[str]
    eTagAlgorithmFamily: NotRequired[ETagAlgorithmFamilyType]
    propagatedSetLevelTags: NotRequired[Sequence[str]]
    s3AccessConfig: NotRequired[S3AccessConfigTypeDef]

UpdateSequenceStoreRequestTypeDef = TypedDict(
    "UpdateSequenceStoreRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
        "fallbackLocation": NotRequired[str],
        "propagatedSetLevelTags": NotRequired[Sequence[str]],
        "s3AccessConfig": NotRequired[S3AccessConfigTypeDef],
    },
)
CreateSequenceStoreResponseTypeDef = TypedDict(
    "CreateSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "fallbackLocation": str,
        "eTagAlgorithmFamily": ETagAlgorithmFamilyType,
        "status": SequenceStoreStatusType,
        "statusMessage": str,
        "propagatedSetLevelTags": List[str],
        "s3Access": SequenceStoreS3AccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSequenceStoreResponseTypeDef = TypedDict(
    "GetSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "fallbackLocation": str,
        "s3Access": SequenceStoreS3AccessTypeDef,
        "eTagAlgorithmFamily": ETagAlgorithmFamilyType,
        "status": SequenceStoreStatusType,
        "statusMessage": str,
        "propagatedSetLevelTags": List[str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSequenceStoreResponseTypeDef = TypedDict(
    "UpdateSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "propagatedSetLevelTags": List[str],
        "status": SequenceStoreStatusType,
        "statusMessage": str,
        "fallbackLocation": str,
        "s3Access": SequenceStoreS3AccessTypeDef,
        "eTagAlgorithmFamily": ETagAlgorithmFamilyType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateWorkflowRequestTypeDef(TypedDict):
    requestId: str
    name: NotRequired[str]
    description: NotRequired[str]
    engine: NotRequired[WorkflowEngineType]
    definitionZip: NotRequired[BlobTypeDef]
    definitionUri: NotRequired[str]
    main: NotRequired[str]
    parameterTemplate: NotRequired[Mapping[str, WorkflowParameterTypeDef]]
    storageCapacity: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    accelerators: NotRequired[Literal["GPU"]]
    storageType: NotRequired[StorageTypeType]

class CreateWorkflowVersionRequestTypeDef(TypedDict):
    workflowId: str
    versionName: str
    requestId: str
    definitionZip: NotRequired[BlobTypeDef]
    definitionUri: NotRequired[str]
    accelerators: NotRequired[Literal["GPU"]]
    description: NotRequired[str]
    engine: NotRequired[WorkflowEngineType]
    main: NotRequired[str]
    parameterTemplate: NotRequired[Mapping[str, WorkflowParameterTypeDef]]
    storageType: NotRequired[StorageTypeType]
    storageCapacity: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    workflowBucketOwnerId: NotRequired[str]

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": WorkflowStatusType,
        "type": WorkflowTypeType,
        "name": str,
        "description": str,
        "engine": WorkflowEngineType,
        "definition": str,
        "main": str,
        "digest": str,
        "parameterTemplate": Dict[str, WorkflowParameterTypeDef],
        "storageCapacity": int,
        "creationTime": datetime,
        "statusMessage": str,
        "tags": Dict[str, str],
        "metadata": Dict[str, str],
        "accelerators": Literal["GPU"],
        "storageType": StorageTypeType,
        "uuid": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowVersionResponseTypeDef = TypedDict(
    "GetWorkflowVersionResponseTypeDef",
    {
        "arn": str,
        "workflowId": str,
        "versionName": str,
        "accelerators": Literal["GPU"],
        "creationTime": datetime,
        "description": str,
        "definition": str,
        "digest": str,
        "engine": WorkflowEngineType,
        "main": str,
        "metadata": Dict[str, str],
        "parameterTemplate": Dict[str, WorkflowParameterTypeDef],
        "status": WorkflowStatusType,
        "statusMessage": str,
        "storageType": StorageTypeType,
        "storageCapacity": int,
        "type": WorkflowTypeType,
        "tags": Dict[str, str],
        "uuid": str,
        "workflowBucketOwnerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteAnnotationStoreVersionsResponseTypeDef(TypedDict):
    errors: List[VersionDeleteErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

GetReadSetExportJobResponseTypeDef = TypedDict(
    "GetReadSetExportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "readSets": List[ExportReadSetDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListReadSetExportJobsResponseTypeDef(TypedDict):
    exportJobs: List[ExportReadSetJobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartReadSetExportJobRequestTypeDef(TypedDict):
    sequenceStoreId: str
    destination: str
    roleArn: str
    sources: Sequence[ExportReadSetTypeDef]
    clientToken: NotRequired[str]

class FileInformationTypeDef(TypedDict):
    totalParts: NotRequired[int]
    partSize: NotRequired[int]
    contentLength: NotRequired[int]
    s3Access: NotRequired[ReadSetS3AccessTypeDef]

ListSharesRequestTypeDef = TypedDict(
    "ListSharesRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "filter": NotRequired[FilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class GetAnnotationImportRequestWaitTypeDef(TypedDict):
    jobId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetAnnotationStoreRequestWaitExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetAnnotationStoreRequestWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetAnnotationStoreVersionRequestWaitExtraTypeDef(TypedDict):
    name: str
    versionName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetAnnotationStoreVersionRequestWaitTypeDef(TypedDict):
    name: str
    versionName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

GetReadSetActivationJobRequestWaitTypeDef = TypedDict(
    "GetReadSetActivationJobRequestWaitTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReadSetExportJobRequestWaitTypeDef = TypedDict(
    "GetReadSetExportJobRequestWaitTypeDef",
    {
        "sequenceStoreId": str,
        "id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReadSetImportJobRequestWaitTypeDef = TypedDict(
    "GetReadSetImportJobRequestWaitTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReferenceImportJobRequestWaitTypeDef = TypedDict(
    "GetReferenceImportJobRequestWaitTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunRequestWaitExtraTypeDef = TypedDict(
    "GetRunRequestWaitExtraTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunRequestWaitTypeDef = TypedDict(
    "GetRunRequestWaitTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunTaskRequestWaitExtraTypeDef = TypedDict(
    "GetRunTaskRequestWaitExtraTypeDef",
    {
        "id": str,
        "taskId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunTaskRequestWaitTypeDef = TypedDict(
    "GetRunTaskRequestWaitTypeDef",
    {
        "id": str,
        "taskId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)

class GetVariantImportRequestWaitTypeDef(TypedDict):
    jobId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetVariantStoreRequestWaitExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetVariantStoreRequestWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

GetWorkflowRequestWaitTypeDef = TypedDict(
    "GetWorkflowRequestWaitTypeDef",
    {
        "id": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetWorkflowVersionRequestWaitTypeDef = TypedDict(
    "GetWorkflowVersionRequestWaitTypeDef",
    {
        "workflowId": str,
        "versionName": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ReadSetListItemTypeDef = TypedDict(
    "ReadSetListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "sequenceStoreId": str,
        "status": ReadSetStatusType,
        "fileType": FileTypeType,
        "creationTime": datetime,
        "subjectId": NotRequired[str],
        "sampleId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "referenceArn": NotRequired[str],
        "sequenceInformation": NotRequired[SequenceInformationTypeDef],
        "statusMessage": NotRequired[str],
        "creationType": NotRequired[CreationTypeType],
        "etag": NotRequired[ETagTypeDef],
    },
)
GetReferenceImportJobResponseTypeDef = TypedDict(
    "GetReferenceImportJobResponseTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ImportReferenceSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunResponseTypeDef = TypedDict(
    "GetRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "cacheId": str,
        "cacheBehavior": CacheBehaviorType,
        "engineVersion": str,
        "status": RunStatusType,
        "workflowId": str,
        "workflowType": WorkflowTypeType,
        "runId": str,
        "roleArn": str,
        "name": str,
        "runGroupId": str,
        "priority": int,
        "definition": str,
        "digest": str,
        "parameters": Dict[str, Any],
        "storageCapacity": int,
        "outputUri": str,
        "logLevel": RunLogLevelType,
        "resourceDigests": Dict[str, str],
        "startedBy": str,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
        "statusMessage": str,
        "tags": Dict[str, str],
        "accelerators": Literal["GPU"],
        "retentionMode": RunRetentionModeType,
        "failureReason": str,
        "logLocation": RunLogLocationTypeDef,
        "uuid": str,
        "runOutputUri": str,
        "storageType": StorageTypeType,
        "workflowOwnerId": str,
        "workflowVersionName": str,
        "workflowUuid": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetShareResponseTypeDef(TypedDict):
    share: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharesResponseTypeDef(TypedDict):
    shares: List[ShareDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetVariantImportResponseTypeDef = TypedDict(
    "GetVariantImportResponseTypeDef",
    {
        "id": str,
        "destinationName": str,
        "roleArn": str,
        "status": JobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": datetime,
        "items": List[VariantImportItemDetailTypeDef],
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListReadSetImportJobsResponseTypeDef(TypedDict):
    importJobs: List[ImportReadSetJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ImportReadSetSourceItemTypeDef(TypedDict):
    sourceFiles: SourceFilesTypeDef
    sourceFileType: FileTypeType
    status: ReadSetImportJobItemStatusType
    subjectId: str
    sampleId: str
    statusMessage: NotRequired[str]
    generatedFrom: NotRequired[str]
    referenceArn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    readSetId: NotRequired[str]

class StartReadSetImportJobSourceItemTypeDef(TypedDict):
    sourceFiles: SourceFilesTypeDef
    sourceFileType: FileTypeType
    subjectId: str
    sampleId: str
    generatedFrom: NotRequired[str]
    referenceArn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ListReferenceImportJobsResponseTypeDef(TypedDict):
    importJobs: List[ImportReferenceJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListAnnotationImportJobsRequestTypeDef = TypedDict(
    "ListAnnotationImportJobsRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationImportJobsFilterTypeDef],
    },
)
ListAnnotationImportJobsRequestPaginateTypeDef = TypedDict(
    "ListAnnotationImportJobsRequestPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListAnnotationImportJobsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListMultipartReadSetUploadsRequestPaginateTypeDef(TypedDict):
    sequenceStoreId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRunCachesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRunGroupsRequestPaginateTypeDef(TypedDict):
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListRunTasksRequestPaginateTypeDef = TypedDict(
    "ListRunTasksRequestPaginateTypeDef",
    {
        "id": str,
        "status": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListRunsRequestPaginateTypeDef(TypedDict):
    name: NotRequired[str]
    runGroupId: NotRequired[str]
    status: NotRequired[RunStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListSharesRequestPaginateTypeDef = TypedDict(
    "ListSharesRequestPaginateTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "filter": NotRequired[FilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowVersionsRequestPaginateTypeDef = TypedDict(
    "ListWorkflowVersionsRequestPaginateTypeDef",
    {
        "workflowId": str,
        "type": NotRequired[WorkflowTypeType],
        "workflowOwnerId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowsRequestPaginateTypeDef = TypedDict(
    "ListWorkflowsRequestPaginateTypeDef",
    {
        "type": NotRequired[WorkflowTypeType],
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoreVersionsRequestPaginateTypeDef = TypedDict(
    "ListAnnotationStoreVersionsRequestPaginateTypeDef",
    {
        "name": str,
        "filter": NotRequired[ListAnnotationStoreVersionsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoreVersionsRequestTypeDef = TypedDict(
    "ListAnnotationStoreVersionsRequestTypeDef",
    {
        "name": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationStoreVersionsFilterTypeDef],
    },
)
ListAnnotationStoresRequestPaginateTypeDef = TypedDict(
    "ListAnnotationStoresRequestPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListAnnotationStoresFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoresRequestTypeDef = TypedDict(
    "ListAnnotationStoresRequestTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationStoresFilterTypeDef],
    },
)

class ListMultipartReadSetUploadsResponseTypeDef(TypedDict):
    uploads: List[MultipartReadSetUploadListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReadSetUploadPartsResponseTypeDef(TypedDict):
    parts: List[ReadSetUploadPartListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReferencesResponseTypeDef(TypedDict):
    references: List[ReferenceListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRunCachesResponseTypeDef(TypedDict):
    items: List[RunCacheListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRunGroupsResponseTypeDef(TypedDict):
    items: List[RunGroupListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRunTasksResponseTypeDef(TypedDict):
    items: List[TaskListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRunsResponseTypeDef(TypedDict):
    items: List[RunListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListVariantImportJobsRequestPaginateTypeDef = TypedDict(
    "ListVariantImportJobsRequestPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListVariantImportJobsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVariantImportJobsRequestTypeDef = TypedDict(
    "ListVariantImportJobsRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListVariantImportJobsFilterTypeDef],
    },
)

class ListVariantImportJobsResponseTypeDef(TypedDict):
    variantImportJobs: List[VariantImportJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListVariantStoresRequestPaginateTypeDef = TypedDict(
    "ListVariantStoresRequestPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListVariantStoresFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVariantStoresRequestTypeDef = TypedDict(
    "ListVariantStoresRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListVariantStoresFilterTypeDef],
    },
)

class ListWorkflowVersionsResponseTypeDef(TypedDict):
    items: List[WorkflowVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowsResponseTypeDef(TypedDict):
    items: List[WorkflowListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TsvOptionsTypeDef(TypedDict):
    readOptions: NotRequired[ReadOptionsTypeDef]

class StartReadSetActivationJobRequestTypeDef(TypedDict):
    sequenceStoreId: str
    sources: Sequence[StartReadSetActivationJobSourceItemTypeDef]
    clientToken: NotRequired[str]

class StartReferenceImportJobRequestTypeDef(TypedDict):
    referenceStoreId: str
    roleArn: str
    sources: Sequence[StartReferenceImportJobSourceItemTypeDef]
    clientToken: NotRequired[str]

class StartVariantImportRequestTypeDef(TypedDict):
    destinationName: str
    roleArn: str
    items: Sequence[VariantImportItemSourceTypeDef]
    runLeftNormalization: NotRequired[bool]
    annotationFields: NotRequired[Mapping[str, str]]

class StoreOptionsOutputTypeDef(TypedDict):
    tsvStoreOptions: NotRequired[TsvStoreOptionsOutputTypeDef]

class StoreOptionsTypeDef(TypedDict):
    tsvStoreOptions: NotRequired[TsvStoreOptionsTypeDef]

class VersionOptionsOutputTypeDef(TypedDict):
    tsvVersionOptions: NotRequired[TsvVersionOptionsOutputTypeDef]

class VersionOptionsTypeDef(TypedDict):
    tsvVersionOptions: NotRequired[TsvVersionOptionsTypeDef]

ListReadSetActivationJobsRequestPaginateTypeDef = TypedDict(
    "ListReadSetActivationJobsRequestPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ActivateReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetActivationJobsRequestTypeDef = TypedDict(
    "ListReadSetActivationJobsRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ActivateReadSetFilterTypeDef],
    },
)
ListReadSetExportJobsRequestPaginateTypeDef = TypedDict(
    "ListReadSetExportJobsRequestPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ExportReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetExportJobsRequestTypeDef = TypedDict(
    "ListReadSetExportJobsRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ExportReadSetFilterTypeDef],
    },
)
ListReadSetImportJobsRequestPaginateTypeDef = TypedDict(
    "ListReadSetImportJobsRequestPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ImportReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetImportJobsRequestTypeDef = TypedDict(
    "ListReadSetImportJobsRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ImportReadSetFilterTypeDef],
    },
)
ListReferenceImportJobsRequestPaginateTypeDef = TypedDict(
    "ListReferenceImportJobsRequestPaginateTypeDef",
    {
        "referenceStoreId": str,
        "filter": NotRequired[ImportReferenceFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferenceImportJobsRequestTypeDef = TypedDict(
    "ListReferenceImportJobsRequestTypeDef",
    {
        "referenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ImportReferenceFilterTypeDef],
    },
)
ListReadSetsRequestPaginateTypeDef = TypedDict(
    "ListReadSetsRequestPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetsRequestTypeDef = TypedDict(
    "ListReadSetsRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReadSetFilterTypeDef],
    },
)
ListReadSetUploadPartsRequestPaginateTypeDef = TypedDict(
    "ListReadSetUploadPartsRequestPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "filter": NotRequired[ReadSetUploadPartListFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetUploadPartsRequestTypeDef = TypedDict(
    "ListReadSetUploadPartsRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReadSetUploadPartListFilterTypeDef],
    },
)
ListReferencesRequestPaginateTypeDef = TypedDict(
    "ListReferencesRequestPaginateTypeDef",
    {
        "referenceStoreId": str,
        "filter": NotRequired[ReferenceFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferencesRequestTypeDef = TypedDict(
    "ListReferencesRequestTypeDef",
    {
        "referenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReferenceFilterTypeDef],
    },
)
ListReferenceStoresRequestPaginateTypeDef = TypedDict(
    "ListReferenceStoresRequestPaginateTypeDef",
    {
        "filter": NotRequired[ReferenceStoreFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferenceStoresRequestTypeDef = TypedDict(
    "ListReferenceStoresRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReferenceStoreFilterTypeDef],
    },
)
ListSequenceStoresRequestPaginateTypeDef = TypedDict(
    "ListSequenceStoresRequestPaginateTypeDef",
    {
        "filter": NotRequired[SequenceStoreFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSequenceStoresRequestTypeDef = TypedDict(
    "ListSequenceStoresRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[SequenceStoreFilterTypeDef],
    },
)

class ListAnnotationStoresResponseTypeDef(TypedDict):
    annotationStores: List[AnnotationStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReferenceStoresResponseTypeDef(TypedDict):
    referenceStores: List[ReferenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSequenceStoresResponseTypeDef(TypedDict):
    sequenceStores: List[SequenceStoreDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVariantStoresResponseTypeDef(TypedDict):
    variantStores: List[VariantStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReadSetFilesTypeDef(TypedDict):
    source1: NotRequired[FileInformationTypeDef]
    source2: NotRequired[FileInformationTypeDef]
    index: NotRequired[FileInformationTypeDef]

class ReferenceFilesTypeDef(TypedDict):
    source: NotRequired[FileInformationTypeDef]
    index: NotRequired[FileInformationTypeDef]

class ListReadSetsResponseTypeDef(TypedDict):
    readSets: List[ReadSetListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetReadSetImportJobResponseTypeDef = TypedDict(
    "GetReadSetImportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ImportReadSetSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class StartReadSetImportJobRequestTypeDef(TypedDict):
    sequenceStoreId: str
    roleArn: str
    sources: Sequence[StartReadSetImportJobSourceItemTypeDef]
    clientToken: NotRequired[str]

class FormatOptionsTypeDef(TypedDict):
    tsvOptions: NotRequired[TsvOptionsTypeDef]
    vcfOptions: NotRequired[VcfOptionsTypeDef]

CreateAnnotationStoreResponseTypeDef = TypedDict(
    "CreateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "storeFormat": StoreFormatType,
        "storeOptions": StoreOptionsOutputTypeDef,
        "status": StoreStatusType,
        "name": str,
        "versionName": str,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationStoreResponseTypeDef = TypedDict(
    "GetAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "storeOptions": StoreOptionsOutputTypeDef,
        "storeFormat": StoreFormatType,
        "statusMessage": str,
        "storeSizeBytes": int,
        "numVersions": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnnotationStoreResponseTypeDef = TypedDict(
    "UpdateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "storeOptions": StoreOptionsOutputTypeDef,
        "storeFormat": StoreFormatType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StoreOptionsUnionTypeDef = Union[StoreOptionsTypeDef, StoreOptionsOutputTypeDef]
CreateAnnotationStoreVersionResponseTypeDef = TypedDict(
    "CreateAnnotationStoreVersionResponseTypeDef",
    {
        "id": str,
        "versionName": str,
        "storeId": str,
        "versionOptions": VersionOptionsOutputTypeDef,
        "name": str,
        "status": VersionStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationStoreVersionResponseTypeDef = TypedDict(
    "GetAnnotationStoreVersionResponseTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "versionArn": str,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "versionOptions": VersionOptionsOutputTypeDef,
        "statusMessage": str,
        "versionSizeBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VersionOptionsUnionTypeDef = Union[VersionOptionsTypeDef, VersionOptionsOutputTypeDef]
GetReadSetMetadataResponseTypeDef = TypedDict(
    "GetReadSetMetadataResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "sequenceStoreId": str,
        "subjectId": str,
        "sampleId": str,
        "status": ReadSetStatusType,
        "name": str,
        "description": str,
        "fileType": FileTypeType,
        "creationTime": datetime,
        "sequenceInformation": SequenceInformationTypeDef,
        "referenceArn": str,
        "files": ReadSetFilesTypeDef,
        "statusMessage": str,
        "creationType": CreationTypeType,
        "etag": ETagTypeDef,
        "creationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReferenceMetadataResponseTypeDef = TypedDict(
    "GetReferenceMetadataResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "referenceStoreId": str,
        "md5": str,
        "status": ReferenceStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "files": ReferenceFilesTypeDef,
        "creationType": Literal["IMPORT"],
        "creationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationImportResponseTypeDef = TypedDict(
    "GetAnnotationImportResponseTypeDef",
    {
        "id": str,
        "destinationName": str,
        "versionName": str,
        "roleArn": str,
        "status": JobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": datetime,
        "items": List[AnnotationImportItemDetailTypeDef],
        "runLeftNormalization": bool,
        "formatOptions": FormatOptionsTypeDef,
        "annotationFields": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class StartAnnotationImportRequestTypeDef(TypedDict):
    destinationName: str
    roleArn: str
    items: Sequence[AnnotationImportItemSourceTypeDef]
    versionName: NotRequired[str]
    formatOptions: NotRequired[FormatOptionsTypeDef]
    runLeftNormalization: NotRequired[bool]
    annotationFields: NotRequired[Mapping[str, str]]

class CreateAnnotationStoreRequestTypeDef(TypedDict):
    storeFormat: StoreFormatType
    reference: NotRequired[ReferenceItemTypeDef]
    name: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    versionName: NotRequired[str]
    sseConfig: NotRequired[SseConfigTypeDef]
    storeOptions: NotRequired[StoreOptionsUnionTypeDef]

class CreateAnnotationStoreVersionRequestTypeDef(TypedDict):
    name: str
    versionName: str
    description: NotRequired[str]
    versionOptions: NotRequired[VersionOptionsUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
