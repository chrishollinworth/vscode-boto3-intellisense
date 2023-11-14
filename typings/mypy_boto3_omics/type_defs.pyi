"""
Type annotations for omics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_omics.type_defs import AbortMultipartReadSetUploadRequestRequestTypeDef

    data: AbortMultipartReadSetUploadRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AnnotationTypeType,
    CreationTypeType,
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
    RunLogLevelType,
    RunRetentionModeType,
    RunStatusType,
    SchemaValueTypeType,
    ShareStatusType,
    StoreFormatType,
    StoreStatusType,
    TaskStatusType,
    VersionStatusType,
    WorkflowEngineType,
    WorkflowStatusType,
    WorkflowTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AbortMultipartReadSetUploadRequestRequestTypeDef",
    "AcceptShareRequestRequestTypeDef",
    "AcceptShareResponseTypeDef",
    "ActivateReadSetFilterTypeDef",
    "ActivateReadSetJobItemTypeDef",
    "ActivateReadSetSourceItemTypeDef",
    "AnnotationImportItemDetailTypeDef",
    "AnnotationImportItemSourceTypeDef",
    "AnnotationImportJobItemTypeDef",
    "AnnotationStoreItemTypeDef",
    "AnnotationStoreVersionItemTypeDef",
    "BatchDeleteReadSetRequestRequestTypeDef",
    "BatchDeleteReadSetResponseTypeDef",
    "CancelAnnotationImportRequestRequestTypeDef",
    "CancelRunRequestRequestTypeDef",
    "CancelVariantImportRequestRequestTypeDef",
    "CompleteMultipartReadSetUploadRequestRequestTypeDef",
    "CompleteMultipartReadSetUploadResponseTypeDef",
    "CompleteReadSetUploadPartListItemTypeDef",
    "CreateAnnotationStoreRequestRequestTypeDef",
    "CreateAnnotationStoreResponseTypeDef",
    "CreateAnnotationStoreVersionRequestRequestTypeDef",
    "CreateAnnotationStoreVersionResponseTypeDef",
    "CreateMultipartReadSetUploadRequestRequestTypeDef",
    "CreateMultipartReadSetUploadResponseTypeDef",
    "CreateReferenceStoreRequestRequestTypeDef",
    "CreateReferenceStoreResponseTypeDef",
    "CreateRunGroupRequestRequestTypeDef",
    "CreateRunGroupResponseTypeDef",
    "CreateSequenceStoreRequestRequestTypeDef",
    "CreateSequenceStoreResponseTypeDef",
    "CreateShareRequestRequestTypeDef",
    "CreateShareResponseTypeDef",
    "CreateVariantStoreRequestRequestTypeDef",
    "CreateVariantStoreResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DeleteAnnotationStoreRequestRequestTypeDef",
    "DeleteAnnotationStoreResponseTypeDef",
    "DeleteAnnotationStoreVersionsRequestRequestTypeDef",
    "DeleteAnnotationStoreVersionsResponseTypeDef",
    "DeleteReferenceRequestRequestTypeDef",
    "DeleteReferenceStoreRequestRequestTypeDef",
    "DeleteRunGroupRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteSequenceStoreRequestRequestTypeDef",
    "DeleteShareRequestRequestTypeDef",
    "DeleteShareResponseTypeDef",
    "DeleteVariantStoreRequestRequestTypeDef",
    "DeleteVariantStoreResponseTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "ETagTypeDef",
    "ExportReadSetDetailTypeDef",
    "ExportReadSetFilterTypeDef",
    "ExportReadSetJobDetailTypeDef",
    "ExportReadSetTypeDef",
    "FileInformationTypeDef",
    "FilterTypeDef",
    "FormatOptionsTypeDef",
    "GetAnnotationImportRequestRequestTypeDef",
    "GetAnnotationImportResponseTypeDef",
    "GetAnnotationStoreRequestRequestTypeDef",
    "GetAnnotationStoreResponseTypeDef",
    "GetAnnotationStoreVersionRequestRequestTypeDef",
    "GetAnnotationStoreVersionResponseTypeDef",
    "GetReadSetActivationJobRequestRequestTypeDef",
    "GetReadSetActivationJobResponseTypeDef",
    "GetReadSetExportJobRequestRequestTypeDef",
    "GetReadSetExportJobResponseTypeDef",
    "GetReadSetImportJobRequestRequestTypeDef",
    "GetReadSetImportJobResponseTypeDef",
    "GetReadSetMetadataRequestRequestTypeDef",
    "GetReadSetMetadataResponseTypeDef",
    "GetReadSetRequestRequestTypeDef",
    "GetReadSetResponseTypeDef",
    "GetReferenceImportJobRequestRequestTypeDef",
    "GetReferenceImportJobResponseTypeDef",
    "GetReferenceMetadataRequestRequestTypeDef",
    "GetReferenceMetadataResponseTypeDef",
    "GetReferenceRequestRequestTypeDef",
    "GetReferenceResponseTypeDef",
    "GetReferenceStoreRequestRequestTypeDef",
    "GetReferenceStoreResponseTypeDef",
    "GetRunGroupRequestRequestTypeDef",
    "GetRunGroupResponseTypeDef",
    "GetRunRequestRequestTypeDef",
    "GetRunResponseTypeDef",
    "GetRunTaskRequestRequestTypeDef",
    "GetRunTaskResponseTypeDef",
    "GetSequenceStoreRequestRequestTypeDef",
    "GetSequenceStoreResponseTypeDef",
    "GetShareRequestRequestTypeDef",
    "GetShareResponseTypeDef",
    "GetVariantImportRequestRequestTypeDef",
    "GetVariantImportResponseTypeDef",
    "GetVariantStoreRequestRequestTypeDef",
    "GetVariantStoreResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "ImportReadSetFilterTypeDef",
    "ImportReadSetJobItemTypeDef",
    "ImportReadSetSourceItemTypeDef",
    "ImportReferenceFilterTypeDef",
    "ImportReferenceJobItemTypeDef",
    "ImportReferenceSourceItemTypeDef",
    "ListAnnotationImportJobsFilterTypeDef",
    "ListAnnotationImportJobsRequestRequestTypeDef",
    "ListAnnotationImportJobsResponseTypeDef",
    "ListAnnotationStoreVersionsFilterTypeDef",
    "ListAnnotationStoreVersionsRequestRequestTypeDef",
    "ListAnnotationStoreVersionsResponseTypeDef",
    "ListAnnotationStoresFilterTypeDef",
    "ListAnnotationStoresRequestRequestTypeDef",
    "ListAnnotationStoresResponseTypeDef",
    "ListMultipartReadSetUploadsRequestRequestTypeDef",
    "ListMultipartReadSetUploadsResponseTypeDef",
    "ListReadSetActivationJobsRequestRequestTypeDef",
    "ListReadSetActivationJobsResponseTypeDef",
    "ListReadSetExportJobsRequestRequestTypeDef",
    "ListReadSetExportJobsResponseTypeDef",
    "ListReadSetImportJobsRequestRequestTypeDef",
    "ListReadSetImportJobsResponseTypeDef",
    "ListReadSetUploadPartsRequestRequestTypeDef",
    "ListReadSetUploadPartsResponseTypeDef",
    "ListReadSetsRequestRequestTypeDef",
    "ListReadSetsResponseTypeDef",
    "ListReferenceImportJobsRequestRequestTypeDef",
    "ListReferenceImportJobsResponseTypeDef",
    "ListReferenceStoresRequestRequestTypeDef",
    "ListReferenceStoresResponseTypeDef",
    "ListReferencesRequestRequestTypeDef",
    "ListReferencesResponseTypeDef",
    "ListRunGroupsRequestRequestTypeDef",
    "ListRunGroupsResponseTypeDef",
    "ListRunTasksRequestRequestTypeDef",
    "ListRunTasksResponseTypeDef",
    "ListRunsRequestRequestTypeDef",
    "ListRunsResponseTypeDef",
    "ListSequenceStoresRequestRequestTypeDef",
    "ListSequenceStoresResponseTypeDef",
    "ListSharesRequestRequestTypeDef",
    "ListSharesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVariantImportJobsFilterTypeDef",
    "ListVariantImportJobsRequestRequestTypeDef",
    "ListVariantImportJobsResponseTypeDef",
    "ListVariantStoresFilterTypeDef",
    "ListVariantStoresRequestRequestTypeDef",
    "ListVariantStoresResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MultipartReadSetUploadListItemTypeDef",
    "PaginatorConfigTypeDef",
    "ReadOptionsTypeDef",
    "ReadSetBatchErrorTypeDef",
    "ReadSetFilesTypeDef",
    "ReadSetFilterTypeDef",
    "ReadSetListItemTypeDef",
    "ReadSetUploadPartListFilterTypeDef",
    "ReadSetUploadPartListItemTypeDef",
    "ReferenceFilesTypeDef",
    "ReferenceFilterTypeDef",
    "ReferenceItemTypeDef",
    "ReferenceListItemTypeDef",
    "ReferenceStoreDetailTypeDef",
    "ReferenceStoreFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RunGroupListItemTypeDef",
    "RunListItemTypeDef",
    "RunLogLocationTypeDef",
    "SequenceInformationTypeDef",
    "SequenceStoreDetailTypeDef",
    "SequenceStoreFilterTypeDef",
    "ShareDetailsTypeDef",
    "SourceFilesTypeDef",
    "SseConfigTypeDef",
    "StartAnnotationImportRequestRequestTypeDef",
    "StartAnnotationImportResponseTypeDef",
    "StartReadSetActivationJobRequestRequestTypeDef",
    "StartReadSetActivationJobResponseTypeDef",
    "StartReadSetActivationJobSourceItemTypeDef",
    "StartReadSetExportJobRequestRequestTypeDef",
    "StartReadSetExportJobResponseTypeDef",
    "StartReadSetImportJobRequestRequestTypeDef",
    "StartReadSetImportJobResponseTypeDef",
    "StartReadSetImportJobSourceItemTypeDef",
    "StartReferenceImportJobRequestRequestTypeDef",
    "StartReferenceImportJobResponseTypeDef",
    "StartReferenceImportJobSourceItemTypeDef",
    "StartRunRequestRequestTypeDef",
    "StartRunResponseTypeDef",
    "StartVariantImportRequestRequestTypeDef",
    "StartVariantImportResponseTypeDef",
    "StoreOptionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskListItemTypeDef",
    "TsvOptionsTypeDef",
    "TsvStoreOptionsTypeDef",
    "TsvVersionOptionsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnnotationStoreRequestRequestTypeDef",
    "UpdateAnnotationStoreResponseTypeDef",
    "UpdateAnnotationStoreVersionRequestRequestTypeDef",
    "UpdateAnnotationStoreVersionResponseTypeDef",
    "UpdateRunGroupRequestRequestTypeDef",
    "UpdateVariantStoreRequestRequestTypeDef",
    "UpdateVariantStoreResponseTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "UploadReadSetPartRequestRequestTypeDef",
    "UploadReadSetPartResponseTypeDef",
    "VariantImportItemDetailTypeDef",
    "VariantImportItemSourceTypeDef",
    "VariantImportJobItemTypeDef",
    "VariantStoreItemTypeDef",
    "VcfOptionsTypeDef",
    "VersionDeleteErrorTypeDef",
    "VersionOptionsTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowListItemTypeDef",
    "WorkflowParameterTypeDef",
)

AbortMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "AbortMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
    },
)

AcceptShareRequestRequestTypeDef = TypedDict(
    "AcceptShareRequestRequestTypeDef",
    {
        "shareId": str,
    },
)

AcceptShareResponseTypeDef = TypedDict(
    "AcceptShareResponseTypeDef",
    {
        "status": ShareStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActivateReadSetFilterTypeDef = TypedDict(
    "ActivateReadSetFilterTypeDef",
    {
        "status": ReadSetActivationJobStatusType,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

_RequiredActivateReadSetJobItemTypeDef = TypedDict(
    "_RequiredActivateReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
    },
)
_OptionalActivateReadSetJobItemTypeDef = TypedDict(
    "_OptionalActivateReadSetJobItemTypeDef",
    {
        "completionTime": datetime,
    },
    total=False,
)

class ActivateReadSetJobItemTypeDef(
    _RequiredActivateReadSetJobItemTypeDef, _OptionalActivateReadSetJobItemTypeDef
):
    pass

_RequiredActivateReadSetSourceItemTypeDef = TypedDict(
    "_RequiredActivateReadSetSourceItemTypeDef",
    {
        "readSetId": str,
        "status": ReadSetActivationJobItemStatusType,
    },
)
_OptionalActivateReadSetSourceItemTypeDef = TypedDict(
    "_OptionalActivateReadSetSourceItemTypeDef",
    {
        "statusMessage": str,
    },
    total=False,
)

class ActivateReadSetSourceItemTypeDef(
    _RequiredActivateReadSetSourceItemTypeDef, _OptionalActivateReadSetSourceItemTypeDef
):
    pass

AnnotationImportItemDetailTypeDef = TypedDict(
    "AnnotationImportItemDetailTypeDef",
    {
        "source": str,
        "jobStatus": JobStatusType,
    },
)

AnnotationImportItemSourceTypeDef = TypedDict(
    "AnnotationImportItemSourceTypeDef",
    {
        "source": str,
    },
)

_RequiredAnnotationImportJobItemTypeDef = TypedDict(
    "_RequiredAnnotationImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "versionName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalAnnotationImportJobItemTypeDef = TypedDict(
    "_OptionalAnnotationImportJobItemTypeDef",
    {
        "completionTime": datetime,
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
    },
    total=False,
)

class AnnotationImportJobItemTypeDef(
    _RequiredAnnotationImportJobItemTypeDef, _OptionalAnnotationImportJobItemTypeDef
):
    pass

AnnotationStoreItemTypeDef = TypedDict(
    "AnnotationStoreItemTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "storeFormat": StoreFormatType,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
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

BatchDeleteReadSetRequestRequestTypeDef = TypedDict(
    "BatchDeleteReadSetRequestRequestTypeDef",
    {
        "ids": List[str],
        "sequenceStoreId": str,
    },
)

BatchDeleteReadSetResponseTypeDef = TypedDict(
    "BatchDeleteReadSetResponseTypeDef",
    {
        "errors": List["ReadSetBatchErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelAnnotationImportRequestRequestTypeDef = TypedDict(
    "CancelAnnotationImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CancelRunRequestRequestTypeDef = TypedDict(
    "CancelRunRequestRequestTypeDef",
    {
        "id": str,
    },
)

CancelVariantImportRequestRequestTypeDef = TypedDict(
    "CancelVariantImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CompleteMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "CompleteMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "parts": List["CompleteReadSetUploadPartListItemTypeDef"],
    },
)

CompleteMultipartReadSetUploadResponseTypeDef = TypedDict(
    "CompleteMultipartReadSetUploadResponseTypeDef",
    {
        "readSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompleteReadSetUploadPartListItemTypeDef = TypedDict(
    "CompleteReadSetUploadPartListItemTypeDef",
    {
        "partNumber": int,
        "partSource": ReadSetPartSourceType,
        "checksum": str,
    },
)

_RequiredCreateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnnotationStoreRequestRequestTypeDef",
    {
        "storeFormat": StoreFormatType,
    },
)
_OptionalCreateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnnotationStoreRequestRequestTypeDef",
    {
        "reference": "ReferenceItemTypeDef",
        "name": str,
        "description": str,
        "tags": Dict[str, str],
        "versionName": str,
        "sseConfig": "SseConfigTypeDef",
        "storeOptions": "StoreOptionsTypeDef",
    },
    total=False,
)

class CreateAnnotationStoreRequestRequestTypeDef(
    _RequiredCreateAnnotationStoreRequestRequestTypeDef,
    _OptionalCreateAnnotationStoreRequestRequestTypeDef,
):
    pass

CreateAnnotationStoreResponseTypeDef = TypedDict(
    "CreateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "storeFormat": StoreFormatType,
        "storeOptions": "StoreOptionsTypeDef",
        "status": StoreStatusType,
        "name": str,
        "versionName": str,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
    },
)
_OptionalCreateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "description": str,
        "versionOptions": "VersionOptionsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAnnotationStoreVersionRequestRequestTypeDef(
    _RequiredCreateAnnotationStoreVersionRequestRequestTypeDef,
    _OptionalCreateAnnotationStoreVersionRequestRequestTypeDef,
):
    pass

CreateAnnotationStoreVersionResponseTypeDef = TypedDict(
    "CreateAnnotationStoreVersionResponseTypeDef",
    {
        "id": str,
        "versionName": str,
        "storeId": str,
        "versionOptions": "VersionOptionsTypeDef",
        "name": str,
        "status": VersionStatusType,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "name": str,
    },
)
_OptionalCreateMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMultipartReadSetUploadRequestRequestTypeDef",
    {
        "clientToken": str,
        "generatedFrom": str,
        "referenceArn": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateMultipartReadSetUploadRequestRequestTypeDef(
    _RequiredCreateMultipartReadSetUploadRequestRequestTypeDef,
    _OptionalCreateMultipartReadSetUploadRequestRequestTypeDef,
):
    pass

CreateMultipartReadSetUploadResponseTypeDef = TypedDict(
    "CreateMultipartReadSetUploadResponseTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "generatedFrom": str,
        "referenceArn": str,
        "name": str,
        "description": str,
        "tags": Dict[str, str],
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReferenceStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReferenceStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateReferenceStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReferenceStoreRequestRequestTypeDef",
    {
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "tags": Dict[str, str],
        "clientToken": str,
    },
    total=False,
)

class CreateReferenceStoreRequestRequestTypeDef(
    _RequiredCreateReferenceStoreRequestRequestTypeDef,
    _OptionalCreateReferenceStoreRequestRequestTypeDef,
):
    pass

CreateReferenceStoreResponseTypeDef = TypedDict(
    "CreateReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRunGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRunGroupRequestRequestTypeDef",
    {
        "requestId": str,
    },
)
_OptionalCreateRunGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRunGroupRequestRequestTypeDef",
    {
        "name": str,
        "maxCpus": int,
        "maxRuns": int,
        "maxDuration": int,
        "tags": Dict[str, str],
        "maxGpus": int,
    },
    total=False,
)

class CreateRunGroupRequestRequestTypeDef(
    _RequiredCreateRunGroupRequestRequestTypeDef, _OptionalCreateRunGroupRequestRequestTypeDef
):
    pass

CreateRunGroupResponseTypeDef = TypedDict(
    "CreateRunGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSequenceStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSequenceStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSequenceStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSequenceStoreRequestRequestTypeDef",
    {
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "tags": Dict[str, str],
        "clientToken": str,
        "fallbackLocation": str,
    },
    total=False,
)

class CreateSequenceStoreRequestRequestTypeDef(
    _RequiredCreateSequenceStoreRequestRequestTypeDef,
    _OptionalCreateSequenceStoreRequestRequestTypeDef,
):
    pass

CreateSequenceStoreResponseTypeDef = TypedDict(
    "CreateSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "fallbackLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateShareRequestRequestTypeDef = TypedDict(
    "_RequiredCreateShareRequestRequestTypeDef",
    {
        "resourceArn": str,
        "principalSubscriber": str,
    },
)
_OptionalCreateShareRequestRequestTypeDef = TypedDict(
    "_OptionalCreateShareRequestRequestTypeDef",
    {
        "shareName": str,
    },
    total=False,
)

class CreateShareRequestRequestTypeDef(
    _RequiredCreateShareRequestRequestTypeDef, _OptionalCreateShareRequestRequestTypeDef
):
    pass

CreateShareResponseTypeDef = TypedDict(
    "CreateShareResponseTypeDef",
    {
        "shareId": str,
        "status": ShareStatusType,
        "shareName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVariantStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVariantStoreRequestRequestTypeDef",
    {
        "reference": "ReferenceItemTypeDef",
    },
)
_OptionalCreateVariantStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVariantStoreRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "tags": Dict[str, str],
        "sseConfig": "SseConfigTypeDef",
    },
    total=False,
)

class CreateVariantStoreRequestRequestTypeDef(
    _RequiredCreateVariantStoreRequestRequestTypeDef,
    _OptionalCreateVariantStoreRequestRequestTypeDef,
):
    pass

CreateVariantStoreResponseTypeDef = TypedDict(
    "CreateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "name": str,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkflowRequestRequestTypeDef",
    {
        "requestId": str,
    },
)
_OptionalCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkflowRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "engine": WorkflowEngineType,
        "definitionZip": Union[bytes, IO[bytes], StreamingBody],
        "definitionUri": str,
        "main": str,
        "parameterTemplate": Dict[str, "WorkflowParameterTypeDef"],
        "storageCapacity": int,
        "tags": Dict[str, str],
        "accelerators": Literal["GPU"],
    },
    total=False,
)

class CreateWorkflowRequestRequestTypeDef(
    _RequiredCreateWorkflowRequestRequestTypeDef, _OptionalCreateWorkflowRequestRequestTypeDef
):
    pass

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": WorkflowStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalDeleteAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnnotationStoreRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteAnnotationStoreRequestRequestTypeDef(
    _RequiredDeleteAnnotationStoreRequestRequestTypeDef,
    _OptionalDeleteAnnotationStoreRequestRequestTypeDef,
):
    pass

DeleteAnnotationStoreResponseTypeDef = TypedDict(
    "DeleteAnnotationStoreResponseTypeDef",
    {
        "status": StoreStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "name": str,
        "versions": List[str],
    },
)
_OptionalDeleteAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteAnnotationStoreVersionsRequestRequestTypeDef(
    _RequiredDeleteAnnotationStoreVersionsRequestRequestTypeDef,
    _OptionalDeleteAnnotationStoreVersionsRequestRequestTypeDef,
):
    pass

DeleteAnnotationStoreVersionsResponseTypeDef = TypedDict(
    "DeleteAnnotationStoreVersionsResponseTypeDef",
    {
        "errors": List["VersionDeleteErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReferenceRequestRequestTypeDef = TypedDict(
    "DeleteReferenceRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)

DeleteReferenceStoreRequestRequestTypeDef = TypedDict(
    "DeleteReferenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteRunGroupRequestRequestTypeDef = TypedDict(
    "DeleteRunGroupRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteSequenceStoreRequestRequestTypeDef = TypedDict(
    "DeleteSequenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteShareRequestRequestTypeDef = TypedDict(
    "DeleteShareRequestRequestTypeDef",
    {
        "shareId": str,
    },
)

DeleteShareResponseTypeDef = TypedDict(
    "DeleteShareResponseTypeDef",
    {
        "status": ShareStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVariantStoreRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVariantStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalDeleteVariantStoreRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVariantStoreRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteVariantStoreRequestRequestTypeDef(
    _RequiredDeleteVariantStoreRequestRequestTypeDef,
    _OptionalDeleteVariantStoreRequestRequestTypeDef,
):
    pass

DeleteVariantStoreResponseTypeDef = TypedDict(
    "DeleteVariantStoreResponseTypeDef",
    {
        "status": StoreStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)

ETagTypeDef = TypedDict(
    "ETagTypeDef",
    {
        "algorithm": ETagAlgorithmType,
        "source1": str,
        "source2": str,
    },
    total=False,
)

_RequiredExportReadSetDetailTypeDef = TypedDict(
    "_RequiredExportReadSetDetailTypeDef",
    {
        "id": str,
        "status": ReadSetExportJobItemStatusType,
    },
)
_OptionalExportReadSetDetailTypeDef = TypedDict(
    "_OptionalExportReadSetDetailTypeDef",
    {
        "statusMessage": str,
    },
    total=False,
)

class ExportReadSetDetailTypeDef(
    _RequiredExportReadSetDetailTypeDef, _OptionalExportReadSetDetailTypeDef
):
    pass

ExportReadSetFilterTypeDef = TypedDict(
    "ExportReadSetFilterTypeDef",
    {
        "status": ReadSetExportJobStatusType,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

_RequiredExportReadSetJobDetailTypeDef = TypedDict(
    "_RequiredExportReadSetJobDetailTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
    },
)
_OptionalExportReadSetJobDetailTypeDef = TypedDict(
    "_OptionalExportReadSetJobDetailTypeDef",
    {
        "completionTime": datetime,
    },
    total=False,
)

class ExportReadSetJobDetailTypeDef(
    _RequiredExportReadSetJobDetailTypeDef, _OptionalExportReadSetJobDetailTypeDef
):
    pass

ExportReadSetTypeDef = TypedDict(
    "ExportReadSetTypeDef",
    {
        "readSetId": str,
    },
)

FileInformationTypeDef = TypedDict(
    "FileInformationTypeDef",
    {
        "totalParts": int,
        "partSize": int,
        "contentLength": int,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "resourceArns": List[str],
        "status": List[ShareStatusType],
    },
    total=False,
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "tsvOptions": "TsvOptionsTypeDef",
        "vcfOptions": "VcfOptionsTypeDef",
    },
    total=False,
)

GetAnnotationImportRequestRequestTypeDef = TypedDict(
    "GetAnnotationImportRequestRequestTypeDef",
    {
        "jobId": str,
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
        "items": List["AnnotationImportItemDetailTypeDef"],
        "runLeftNormalization": bool,
        "formatOptions": "FormatOptionsTypeDef",
        "annotationFields": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnnotationStoreRequestRequestTypeDef = TypedDict(
    "GetAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetAnnotationStoreResponseTypeDef = TypedDict(
    "GetAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "storeOptions": "StoreOptionsTypeDef",
        "storeFormat": StoreFormatType,
        "statusMessage": str,
        "storeSizeBytes": int,
        "numVersions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "GetAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
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
        "versionOptions": "VersionOptionsTypeDef",
        "statusMessage": str,
        "versionSizeBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadSetActivationJobRequestRequestTypeDef = TypedDict(
    "GetReadSetActivationJobRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)

GetReadSetActivationJobResponseTypeDef = TypedDict(
    "GetReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List["ActivateReadSetSourceItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadSetExportJobRequestRequestTypeDef = TypedDict(
    "GetReadSetExportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "id": str,
    },
)

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
        "readSets": List["ExportReadSetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadSetImportJobRequestRequestTypeDef = TypedDict(
    "GetReadSetImportJobRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)

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
        "sources": List["ImportReadSetSourceItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadSetMetadataRequestRequestTypeDef = TypedDict(
    "GetReadSetMetadataRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)

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
        "sequenceInformation": "SequenceInformationTypeDef",
        "referenceArn": str,
        "files": "ReadSetFilesTypeDef",
        "statusMessage": str,
        "creationType": CreationTypeType,
        "etag": "ETagTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReadSetRequestRequestTypeDef = TypedDict(
    "_RequiredGetReadSetRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "partNumber": int,
    },
)
_OptionalGetReadSetRequestRequestTypeDef = TypedDict(
    "_OptionalGetReadSetRequestRequestTypeDef",
    {
        "file": ReadSetFileType,
    },
    total=False,
)

class GetReadSetRequestRequestTypeDef(
    _RequiredGetReadSetRequestRequestTypeDef, _OptionalGetReadSetRequestRequestTypeDef
):
    pass

GetReadSetResponseTypeDef = TypedDict(
    "GetReadSetResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReferenceImportJobRequestRequestTypeDef = TypedDict(
    "GetReferenceImportJobRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
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
        "sources": List["ImportReferenceSourceItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReferenceMetadataRequestRequestTypeDef = TypedDict(
    "GetReferenceMetadataRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
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
        "files": "ReferenceFilesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReferenceRequestRequestTypeDef = TypedDict(
    "_RequiredGetReferenceRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "partNumber": int,
    },
)
_OptionalGetReferenceRequestRequestTypeDef = TypedDict(
    "_OptionalGetReferenceRequestRequestTypeDef",
    {
        "range": str,
        "file": ReferenceFileType,
    },
    total=False,
)

class GetReferenceRequestRequestTypeDef(
    _RequiredGetReferenceRequestRequestTypeDef, _OptionalGetReferenceRequestRequestTypeDef
):
    pass

GetReferenceResponseTypeDef = TypedDict(
    "GetReferenceResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReferenceStoreRequestRequestTypeDef = TypedDict(
    "GetReferenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetReferenceStoreResponseTypeDef = TypedDict(
    "GetReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRunGroupRequestRequestTypeDef = TypedDict(
    "GetRunGroupRequestRequestTypeDef",
    {
        "id": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRunRequestRequestTypeDef = TypedDict(
    "_RequiredGetRunRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetRunRequestRequestTypeDef = TypedDict(
    "_OptionalGetRunRequestRequestTypeDef",
    {
        "export": List[Literal["DEFINITION"]],
    },
    total=False,
)

class GetRunRequestRequestTypeDef(
    _RequiredGetRunRequestRequestTypeDef, _OptionalGetRunRequestRequestTypeDef
):
    pass

GetRunResponseTypeDef = TypedDict(
    "GetRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
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
        "logLocation": "RunLogLocationTypeDef",
        "uuid": str,
        "runOutputUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRunTaskRequestRequestTypeDef = TypedDict(
    "GetRunTaskRequestRequestTypeDef",
    {
        "id": str,
        "taskId": str,
    },
)

GetRunTaskResponseTypeDef = TypedDict(
    "GetRunTaskResponseTypeDef",
    {
        "taskId": str,
        "status": TaskStatusType,
        "name": str,
        "cpus": int,
        "memory": int,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
        "statusMessage": str,
        "logStream": str,
        "gpus": int,
        "instanceType": str,
        "failureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSequenceStoreRequestRequestTypeDef = TypedDict(
    "GetSequenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSequenceStoreResponseTypeDef = TypedDict(
    "GetSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "fallbackLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetShareRequestRequestTypeDef = TypedDict(
    "GetShareRequestRequestTypeDef",
    {
        "shareId": str,
    },
)

GetShareResponseTypeDef = TypedDict(
    "GetShareResponseTypeDef",
    {
        "share": "ShareDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVariantImportRequestRequestTypeDef = TypedDict(
    "GetVariantImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

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
        "items": List["VariantImportItemDetailTypeDef"],
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVariantStoreRequestRequestTypeDef = TypedDict(
    "GetVariantStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetVariantStoreResponseTypeDef = TypedDict(
    "GetVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "statusMessage": str,
        "storeSizeBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRequestRequestTypeDef",
    {
        "type": WorkflowTypeType,
        "export": List[Literal["DEFINITION"]],
    },
    total=False,
)

class GetWorkflowRequestRequestTypeDef(
    _RequiredGetWorkflowRequestRequestTypeDef, _OptionalGetWorkflowRequestRequestTypeDef
):
    pass

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
        "parameterTemplate": Dict[str, "WorkflowParameterTypeDef"],
        "storageCapacity": int,
        "creationTime": datetime,
        "statusMessage": str,
        "tags": Dict[str, str],
        "metadata": Dict[str, str],
        "accelerators": Literal["GPU"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportReadSetFilterTypeDef = TypedDict(
    "ImportReadSetFilterTypeDef",
    {
        "status": ReadSetImportJobStatusType,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

_RequiredImportReadSetJobItemTypeDef = TypedDict(
    "_RequiredImportReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
    },
)
_OptionalImportReadSetJobItemTypeDef = TypedDict(
    "_OptionalImportReadSetJobItemTypeDef",
    {
        "completionTime": datetime,
    },
    total=False,
)

class ImportReadSetJobItemTypeDef(
    _RequiredImportReadSetJobItemTypeDef, _OptionalImportReadSetJobItemTypeDef
):
    pass

_RequiredImportReadSetSourceItemTypeDef = TypedDict(
    "_RequiredImportReadSetSourceItemTypeDef",
    {
        "sourceFiles": "SourceFilesTypeDef",
        "sourceFileType": FileTypeType,
        "status": ReadSetImportJobItemStatusType,
        "subjectId": str,
        "sampleId": str,
    },
)
_OptionalImportReadSetSourceItemTypeDef = TypedDict(
    "_OptionalImportReadSetSourceItemTypeDef",
    {
        "statusMessage": str,
        "generatedFrom": str,
        "referenceArn": str,
        "name": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportReadSetSourceItemTypeDef(
    _RequiredImportReadSetSourceItemTypeDef, _OptionalImportReadSetSourceItemTypeDef
):
    pass

ImportReferenceFilterTypeDef = TypedDict(
    "ImportReferenceFilterTypeDef",
    {
        "status": ReferenceImportJobStatusType,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

_RequiredImportReferenceJobItemTypeDef = TypedDict(
    "_RequiredImportReferenceJobItemTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
    },
)
_OptionalImportReferenceJobItemTypeDef = TypedDict(
    "_OptionalImportReferenceJobItemTypeDef",
    {
        "completionTime": datetime,
    },
    total=False,
)

class ImportReferenceJobItemTypeDef(
    _RequiredImportReferenceJobItemTypeDef, _OptionalImportReferenceJobItemTypeDef
):
    pass

_RequiredImportReferenceSourceItemTypeDef = TypedDict(
    "_RequiredImportReferenceSourceItemTypeDef",
    {
        "status": ReferenceImportJobItemStatusType,
    },
)
_OptionalImportReferenceSourceItemTypeDef = TypedDict(
    "_OptionalImportReferenceSourceItemTypeDef",
    {
        "sourceFile": str,
        "statusMessage": str,
        "name": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportReferenceSourceItemTypeDef(
    _RequiredImportReferenceSourceItemTypeDef, _OptionalImportReferenceSourceItemTypeDef
):
    pass

ListAnnotationImportJobsFilterTypeDef = TypedDict(
    "ListAnnotationImportJobsFilterTypeDef",
    {
        "status": JobStatusType,
        "storeName": str,
    },
    total=False,
)

ListAnnotationImportJobsRequestRequestTypeDef = TypedDict(
    "ListAnnotationImportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "ids": List[str],
        "nextToken": str,
        "filter": "ListAnnotationImportJobsFilterTypeDef",
    },
    total=False,
)

ListAnnotationImportJobsResponseTypeDef = TypedDict(
    "ListAnnotationImportJobsResponseTypeDef",
    {
        "annotationImportJobs": List["AnnotationImportJobItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnnotationStoreVersionsFilterTypeDef = TypedDict(
    "ListAnnotationStoreVersionsFilterTypeDef",
    {
        "status": VersionStatusType,
    },
    total=False,
)

_RequiredListAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ListAnnotationStoreVersionsFilterTypeDef",
    },
    total=False,
)

class ListAnnotationStoreVersionsRequestRequestTypeDef(
    _RequiredListAnnotationStoreVersionsRequestRequestTypeDef,
    _OptionalListAnnotationStoreVersionsRequestRequestTypeDef,
):
    pass

ListAnnotationStoreVersionsResponseTypeDef = TypedDict(
    "ListAnnotationStoreVersionsResponseTypeDef",
    {
        "annotationStoreVersions": List["AnnotationStoreVersionItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnnotationStoresFilterTypeDef = TypedDict(
    "ListAnnotationStoresFilterTypeDef",
    {
        "status": StoreStatusType,
    },
    total=False,
)

ListAnnotationStoresRequestRequestTypeDef = TypedDict(
    "ListAnnotationStoresRequestRequestTypeDef",
    {
        "ids": List[str],
        "maxResults": int,
        "nextToken": str,
        "filter": "ListAnnotationStoresFilterTypeDef",
    },
    total=False,
)

ListAnnotationStoresResponseTypeDef = TypedDict(
    "ListAnnotationStoresResponseTypeDef",
    {
        "annotationStores": List["AnnotationStoreItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMultipartReadSetUploadsRequestRequestTypeDef = TypedDict(
    "_RequiredListMultipartReadSetUploadsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListMultipartReadSetUploadsRequestRequestTypeDef = TypedDict(
    "_OptionalListMultipartReadSetUploadsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListMultipartReadSetUploadsRequestRequestTypeDef(
    _RequiredListMultipartReadSetUploadsRequestRequestTypeDef,
    _OptionalListMultipartReadSetUploadsRequestRequestTypeDef,
):
    pass

ListMultipartReadSetUploadsResponseTypeDef = TypedDict(
    "ListMultipartReadSetUploadsResponseTypeDef",
    {
        "nextToken": str,
        "uploads": List["MultipartReadSetUploadListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReadSetActivationJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetActivationJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListReadSetActivationJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetActivationJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ActivateReadSetFilterTypeDef",
    },
    total=False,
)

class ListReadSetActivationJobsRequestRequestTypeDef(
    _RequiredListReadSetActivationJobsRequestRequestTypeDef,
    _OptionalListReadSetActivationJobsRequestRequestTypeDef,
):
    pass

ListReadSetActivationJobsResponseTypeDef = TypedDict(
    "ListReadSetActivationJobsResponseTypeDef",
    {
        "nextToken": str,
        "activationJobs": List["ActivateReadSetJobItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReadSetExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetExportJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListReadSetExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetExportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ExportReadSetFilterTypeDef",
    },
    total=False,
)

class ListReadSetExportJobsRequestRequestTypeDef(
    _RequiredListReadSetExportJobsRequestRequestTypeDef,
    _OptionalListReadSetExportJobsRequestRequestTypeDef,
):
    pass

ListReadSetExportJobsResponseTypeDef = TypedDict(
    "ListReadSetExportJobsResponseTypeDef",
    {
        "nextToken": str,
        "exportJobs": List["ExportReadSetJobDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReadSetImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetImportJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListReadSetImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetImportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ImportReadSetFilterTypeDef",
    },
    total=False,
)

class ListReadSetImportJobsRequestRequestTypeDef(
    _RequiredListReadSetImportJobsRequestRequestTypeDef,
    _OptionalListReadSetImportJobsRequestRequestTypeDef,
):
    pass

ListReadSetImportJobsResponseTypeDef = TypedDict(
    "ListReadSetImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "importJobs": List["ImportReadSetJobItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReadSetUploadPartsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetUploadPartsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
    },
)
_OptionalListReadSetUploadPartsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetUploadPartsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ReadSetUploadPartListFilterTypeDef",
    },
    total=False,
)

class ListReadSetUploadPartsRequestRequestTypeDef(
    _RequiredListReadSetUploadPartsRequestRequestTypeDef,
    _OptionalListReadSetUploadPartsRequestRequestTypeDef,
):
    pass

ListReadSetUploadPartsResponseTypeDef = TypedDict(
    "ListReadSetUploadPartsResponseTypeDef",
    {
        "nextToken": str,
        "parts": List["ReadSetUploadPartListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReadSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListReadSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ReadSetFilterTypeDef",
    },
    total=False,
)

class ListReadSetsRequestRequestTypeDef(
    _RequiredListReadSetsRequestRequestTypeDef, _OptionalListReadSetsRequestRequestTypeDef
):
    pass

ListReadSetsResponseTypeDef = TypedDict(
    "ListReadSetsResponseTypeDef",
    {
        "nextToken": str,
        "readSets": List["ReadSetListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReferenceImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListReferenceImportJobsRequestRequestTypeDef",
    {
        "referenceStoreId": str,
    },
)
_OptionalListReferenceImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListReferenceImportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ImportReferenceFilterTypeDef",
    },
    total=False,
)

class ListReferenceImportJobsRequestRequestTypeDef(
    _RequiredListReferenceImportJobsRequestRequestTypeDef,
    _OptionalListReferenceImportJobsRequestRequestTypeDef,
):
    pass

ListReferenceImportJobsResponseTypeDef = TypedDict(
    "ListReferenceImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "importJobs": List["ImportReferenceJobItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReferenceStoresRequestRequestTypeDef = TypedDict(
    "ListReferenceStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ReferenceStoreFilterTypeDef",
    },
    total=False,
)

ListReferenceStoresResponseTypeDef = TypedDict(
    "ListReferenceStoresResponseTypeDef",
    {
        "nextToken": str,
        "referenceStores": List["ReferenceStoreDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredListReferencesRequestRequestTypeDef",
    {
        "referenceStoreId": str,
    },
)
_OptionalListReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalListReferencesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "ReferenceFilterTypeDef",
    },
    total=False,
)

class ListReferencesRequestRequestTypeDef(
    _RequiredListReferencesRequestRequestTypeDef, _OptionalListReferencesRequestRequestTypeDef
):
    pass

ListReferencesResponseTypeDef = TypedDict(
    "ListReferencesResponseTypeDef",
    {
        "nextToken": str,
        "references": List["ReferenceListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRunGroupsRequestRequestTypeDef = TypedDict(
    "ListRunGroupsRequestRequestTypeDef",
    {
        "name": str,
        "startingToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRunGroupsResponseTypeDef = TypedDict(
    "ListRunGroupsResponseTypeDef",
    {
        "items": List["RunGroupListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRunTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListRunTasksRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalListRunTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListRunTasksRequestRequestTypeDef",
    {
        "status": TaskStatusType,
        "startingToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListRunTasksRequestRequestTypeDef(
    _RequiredListRunTasksRequestRequestTypeDef, _OptionalListRunTasksRequestRequestTypeDef
):
    pass

ListRunTasksResponseTypeDef = TypedDict(
    "ListRunTasksResponseTypeDef",
    {
        "items": List["TaskListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRunsRequestRequestTypeDef = TypedDict(
    "ListRunsRequestRequestTypeDef",
    {
        "name": str,
        "runGroupId": str,
        "startingToken": str,
        "maxResults": int,
        "status": RunStatusType,
    },
    total=False,
)

ListRunsResponseTypeDef = TypedDict(
    "ListRunsResponseTypeDef",
    {
        "items": List["RunListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSequenceStoresRequestRequestTypeDef = TypedDict(
    "ListSequenceStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "filter": "SequenceStoreFilterTypeDef",
    },
    total=False,
)

ListSequenceStoresResponseTypeDef = TypedDict(
    "ListSequenceStoresResponseTypeDef",
    {
        "nextToken": str,
        "sequenceStores": List["SequenceStoreDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSharesRequestRequestTypeDef = TypedDict(
    "_RequiredListSharesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalListSharesRequestRequestTypeDef = TypedDict(
    "_OptionalListSharesRequestRequestTypeDef",
    {
        "filter": "FilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSharesRequestRequestTypeDef(
    _RequiredListSharesRequestRequestTypeDef, _OptionalListSharesRequestRequestTypeDef
):
    pass

ListSharesResponseTypeDef = TypedDict(
    "ListSharesResponseTypeDef",
    {
        "shares": List["ShareDetailsTypeDef"],
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

ListVariantImportJobsFilterTypeDef = TypedDict(
    "ListVariantImportJobsFilterTypeDef",
    {
        "status": JobStatusType,
        "storeName": str,
    },
    total=False,
)

ListVariantImportJobsRequestRequestTypeDef = TypedDict(
    "ListVariantImportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "ids": List[str],
        "nextToken": str,
        "filter": "ListVariantImportJobsFilterTypeDef",
    },
    total=False,
)

ListVariantImportJobsResponseTypeDef = TypedDict(
    "ListVariantImportJobsResponseTypeDef",
    {
        "variantImportJobs": List["VariantImportJobItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVariantStoresFilterTypeDef = TypedDict(
    "ListVariantStoresFilterTypeDef",
    {
        "status": StoreStatusType,
    },
    total=False,
)

ListVariantStoresRequestRequestTypeDef = TypedDict(
    "ListVariantStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "ids": List[str],
        "nextToken": str,
        "filter": "ListVariantStoresFilterTypeDef",
    },
    total=False,
)

ListVariantStoresResponseTypeDef = TypedDict(
    "ListVariantStoresResponseTypeDef",
    {
        "variantStores": List["VariantStoreItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "type": WorkflowTypeType,
        "name": str,
        "startingToken": str,
        "maxResults": int,
    },
    total=False,
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "items": List["WorkflowListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMultipartReadSetUploadListItemTypeDef = TypedDict(
    "_RequiredMultipartReadSetUploadListItemTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "generatedFrom": str,
        "referenceArn": str,
        "creationTime": datetime,
    },
)
_OptionalMultipartReadSetUploadListItemTypeDef = TypedDict(
    "_OptionalMultipartReadSetUploadListItemTypeDef",
    {
        "name": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class MultipartReadSetUploadListItemTypeDef(
    _RequiredMultipartReadSetUploadListItemTypeDef, _OptionalMultipartReadSetUploadListItemTypeDef
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

ReadOptionsTypeDef = TypedDict(
    "ReadOptionsTypeDef",
    {
        "sep": str,
        "encoding": str,
        "quote": str,
        "quoteAll": bool,
        "escape": str,
        "escapeQuotes": bool,
        "comment": str,
        "header": bool,
        "lineSep": str,
    },
    total=False,
)

ReadSetBatchErrorTypeDef = TypedDict(
    "ReadSetBatchErrorTypeDef",
    {
        "id": str,
        "code": str,
        "message": str,
    },
)

ReadSetFilesTypeDef = TypedDict(
    "ReadSetFilesTypeDef",
    {
        "source1": "FileInformationTypeDef",
        "source2": "FileInformationTypeDef",
        "index": "FileInformationTypeDef",
    },
    total=False,
)

ReadSetFilterTypeDef = TypedDict(
    "ReadSetFilterTypeDef",
    {
        "name": str,
        "status": ReadSetStatusType,
        "referenceArn": str,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "sampleId": str,
        "subjectId": str,
        "generatedFrom": str,
        "creationType": CreationTypeType,
    },
    total=False,
)

_RequiredReadSetListItemTypeDef = TypedDict(
    "_RequiredReadSetListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "sequenceStoreId": str,
        "status": ReadSetStatusType,
        "fileType": FileTypeType,
        "creationTime": datetime,
    },
)
_OptionalReadSetListItemTypeDef = TypedDict(
    "_OptionalReadSetListItemTypeDef",
    {
        "subjectId": str,
        "sampleId": str,
        "name": str,
        "description": str,
        "referenceArn": str,
        "sequenceInformation": "SequenceInformationTypeDef",
        "statusMessage": str,
        "creationType": CreationTypeType,
        "etag": "ETagTypeDef",
    },
    total=False,
)

class ReadSetListItemTypeDef(_RequiredReadSetListItemTypeDef, _OptionalReadSetListItemTypeDef):
    pass

ReadSetUploadPartListFilterTypeDef = TypedDict(
    "ReadSetUploadPartListFilterTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

_RequiredReadSetUploadPartListItemTypeDef = TypedDict(
    "_RequiredReadSetUploadPartListItemTypeDef",
    {
        "partNumber": int,
        "partSize": int,
        "partSource": ReadSetPartSourceType,
        "checksum": str,
    },
)
_OptionalReadSetUploadPartListItemTypeDef = TypedDict(
    "_OptionalReadSetUploadPartListItemTypeDef",
    {
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

class ReadSetUploadPartListItemTypeDef(
    _RequiredReadSetUploadPartListItemTypeDef, _OptionalReadSetUploadPartListItemTypeDef
):
    pass

ReferenceFilesTypeDef = TypedDict(
    "ReferenceFilesTypeDef",
    {
        "source": "FileInformationTypeDef",
        "index": "FileInformationTypeDef",
    },
    total=False,
)

ReferenceFilterTypeDef = TypedDict(
    "ReferenceFilterTypeDef",
    {
        "name": str,
        "md5": str,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

ReferenceItemTypeDef = TypedDict(
    "ReferenceItemTypeDef",
    {
        "referenceArn": str,
    },
    total=False,
)

_RequiredReferenceListItemTypeDef = TypedDict(
    "_RequiredReferenceListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "referenceStoreId": str,
        "md5": str,
        "creationTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalReferenceListItemTypeDef = TypedDict(
    "_OptionalReferenceListItemTypeDef",
    {
        "status": ReferenceStatusType,
        "name": str,
        "description": str,
    },
    total=False,
)

class ReferenceListItemTypeDef(
    _RequiredReferenceListItemTypeDef, _OptionalReferenceListItemTypeDef
):
    pass

_RequiredReferenceStoreDetailTypeDef = TypedDict(
    "_RequiredReferenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
    },
)
_OptionalReferenceStoreDetailTypeDef = TypedDict(
    "_OptionalReferenceStoreDetailTypeDef",
    {
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
    },
    total=False,
)

class ReferenceStoreDetailTypeDef(
    _RequiredReferenceStoreDetailTypeDef, _OptionalReferenceStoreDetailTypeDef
):
    pass

ReferenceStoreFilterTypeDef = TypedDict(
    "ReferenceStoreFilterTypeDef",
    {
        "name": str,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
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

RunGroupListItemTypeDef = TypedDict(
    "RunGroupListItemTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "maxCpus": int,
        "maxRuns": int,
        "maxDuration": int,
        "creationTime": datetime,
        "maxGpus": int,
    },
    total=False,
)

RunListItemTypeDef = TypedDict(
    "RunListItemTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunStatusType,
        "workflowId": str,
        "name": str,
        "priority": int,
        "storageCapacity": int,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
    },
    total=False,
)

RunLogLocationTypeDef = TypedDict(
    "RunLogLocationTypeDef",
    {
        "engineLogStream": str,
        "runLogStream": str,
    },
    total=False,
)

SequenceInformationTypeDef = TypedDict(
    "SequenceInformationTypeDef",
    {
        "totalReadCount": int,
        "totalBaseCount": int,
        "generatedFrom": str,
        "alignment": str,
    },
    total=False,
)

_RequiredSequenceStoreDetailTypeDef = TypedDict(
    "_RequiredSequenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
    },
)
_OptionalSequenceStoreDetailTypeDef = TypedDict(
    "_OptionalSequenceStoreDetailTypeDef",
    {
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "fallbackLocation": str,
    },
    total=False,
)

class SequenceStoreDetailTypeDef(
    _RequiredSequenceStoreDetailTypeDef, _OptionalSequenceStoreDetailTypeDef
):
    pass

SequenceStoreFilterTypeDef = TypedDict(
    "SequenceStoreFilterTypeDef",
    {
        "name": str,
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
    },
    total=False,
)

ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "shareId": str,
        "resourceArn": str,
        "principalSubscriber": str,
        "ownerId": str,
        "status": ShareStatusType,
        "statusMessage": str,
        "shareName": str,
        "creationTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

_RequiredSourceFilesTypeDef = TypedDict(
    "_RequiredSourceFilesTypeDef",
    {
        "source1": str,
    },
)
_OptionalSourceFilesTypeDef = TypedDict(
    "_OptionalSourceFilesTypeDef",
    {
        "source2": str,
    },
    total=False,
)

class SourceFilesTypeDef(_RequiredSourceFilesTypeDef, _OptionalSourceFilesTypeDef):
    pass

_RequiredSseConfigTypeDef = TypedDict(
    "_RequiredSseConfigTypeDef",
    {
        "type": Literal["KMS"],
    },
)
_OptionalSseConfigTypeDef = TypedDict(
    "_OptionalSseConfigTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)

class SseConfigTypeDef(_RequiredSseConfigTypeDef, _OptionalSseConfigTypeDef):
    pass

_RequiredStartAnnotationImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartAnnotationImportRequestRequestTypeDef",
    {
        "destinationName": str,
        "roleArn": str,
        "items": List["AnnotationImportItemSourceTypeDef"],
    },
)
_OptionalStartAnnotationImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartAnnotationImportRequestRequestTypeDef",
    {
        "versionName": str,
        "formatOptions": "FormatOptionsTypeDef",
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
    },
    total=False,
)

class StartAnnotationImportRequestRequestTypeDef(
    _RequiredStartAnnotationImportRequestRequestTypeDef,
    _OptionalStartAnnotationImportRequestRequestTypeDef,
):
    pass

StartAnnotationImportResponseTypeDef = TypedDict(
    "StartAnnotationImportResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReadSetActivationJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartReadSetActivationJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "sources": List["StartReadSetActivationJobSourceItemTypeDef"],
    },
)
_OptionalStartReadSetActivationJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartReadSetActivationJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartReadSetActivationJobRequestRequestTypeDef(
    _RequiredStartReadSetActivationJobRequestRequestTypeDef,
    _OptionalStartReadSetActivationJobRequestRequestTypeDef,
):
    pass

StartReadSetActivationJobResponseTypeDef = TypedDict(
    "StartReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReadSetActivationJobSourceItemTypeDef = TypedDict(
    "StartReadSetActivationJobSourceItemTypeDef",
    {
        "readSetId": str,
    },
)

_RequiredStartReadSetExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartReadSetExportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "destination": str,
        "roleArn": str,
        "sources": List["ExportReadSetTypeDef"],
    },
)
_OptionalStartReadSetExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartReadSetExportJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartReadSetExportJobRequestRequestTypeDef(
    _RequiredStartReadSetExportJobRequestRequestTypeDef,
    _OptionalStartReadSetExportJobRequestRequestTypeDef,
):
    pass

StartReadSetExportJobResponseTypeDef = TypedDict(
    "StartReadSetExportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReadSetImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartReadSetImportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "roleArn": str,
        "sources": List["StartReadSetImportJobSourceItemTypeDef"],
    },
)
_OptionalStartReadSetImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartReadSetImportJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartReadSetImportJobRequestRequestTypeDef(
    _RequiredStartReadSetImportJobRequestRequestTypeDef,
    _OptionalStartReadSetImportJobRequestRequestTypeDef,
):
    pass

StartReadSetImportJobResponseTypeDef = TypedDict(
    "StartReadSetImportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReadSetImportJobSourceItemTypeDef = TypedDict(
    "_RequiredStartReadSetImportJobSourceItemTypeDef",
    {
        "sourceFiles": "SourceFilesTypeDef",
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
    },
)
_OptionalStartReadSetImportJobSourceItemTypeDef = TypedDict(
    "_OptionalStartReadSetImportJobSourceItemTypeDef",
    {
        "generatedFrom": str,
        "referenceArn": str,
        "name": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartReadSetImportJobSourceItemTypeDef(
    _RequiredStartReadSetImportJobSourceItemTypeDef, _OptionalStartReadSetImportJobSourceItemTypeDef
):
    pass

_RequiredStartReferenceImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartReferenceImportJobRequestRequestTypeDef",
    {
        "referenceStoreId": str,
        "roleArn": str,
        "sources": List["StartReferenceImportJobSourceItemTypeDef"],
    },
)
_OptionalStartReferenceImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartReferenceImportJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartReferenceImportJobRequestRequestTypeDef(
    _RequiredStartReferenceImportJobRequestRequestTypeDef,
    _OptionalStartReferenceImportJobRequestRequestTypeDef,
):
    pass

StartReferenceImportJobResponseTypeDef = TypedDict(
    "StartReferenceImportJobResponseTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReferenceImportJobSourceItemTypeDef = TypedDict(
    "_RequiredStartReferenceImportJobSourceItemTypeDef",
    {
        "sourceFile": str,
        "name": str,
    },
)
_OptionalStartReferenceImportJobSourceItemTypeDef = TypedDict(
    "_OptionalStartReferenceImportJobSourceItemTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartReferenceImportJobSourceItemTypeDef(
    _RequiredStartReferenceImportJobSourceItemTypeDef,
    _OptionalStartReferenceImportJobSourceItemTypeDef,
):
    pass

_RequiredStartRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartRunRequestRequestTypeDef",
    {
        "roleArn": str,
        "requestId": str,
    },
)
_OptionalStartRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartRunRequestRequestTypeDef",
    {
        "workflowId": str,
        "workflowType": WorkflowTypeType,
        "runId": str,
        "name": str,
        "runGroupId": str,
        "priority": int,
        "parameters": Dict[str, Any],
        "storageCapacity": int,
        "outputUri": str,
        "logLevel": RunLogLevelType,
        "tags": Dict[str, str],
        "retentionMode": RunRetentionModeType,
    },
    total=False,
)

class StartRunRequestRequestTypeDef(
    _RequiredStartRunRequestRequestTypeDef, _OptionalStartRunRequestRequestTypeDef
):
    pass

StartRunResponseTypeDef = TypedDict(
    "StartRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunStatusType,
        "tags": Dict[str, str],
        "uuid": str,
        "runOutputUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVariantImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartVariantImportRequestRequestTypeDef",
    {
        "destinationName": str,
        "roleArn": str,
        "items": List["VariantImportItemSourceTypeDef"],
    },
)
_OptionalStartVariantImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartVariantImportRequestRequestTypeDef",
    {
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
    },
    total=False,
)

class StartVariantImportRequestRequestTypeDef(
    _RequiredStartVariantImportRequestRequestTypeDef,
    _OptionalStartVariantImportRequestRequestTypeDef,
):
    pass

StartVariantImportResponseTypeDef = TypedDict(
    "StartVariantImportResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StoreOptionsTypeDef = TypedDict(
    "StoreOptionsTypeDef",
    {
        "tsvStoreOptions": "TsvStoreOptionsTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TaskListItemTypeDef = TypedDict(
    "TaskListItemTypeDef",
    {
        "taskId": str,
        "status": TaskStatusType,
        "name": str,
        "cpus": int,
        "memory": int,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
        "gpus": int,
        "instanceType": str,
    },
    total=False,
)

TsvOptionsTypeDef = TypedDict(
    "TsvOptionsTypeDef",
    {
        "readOptions": "ReadOptionsTypeDef",
    },
    total=False,
)

TsvStoreOptionsTypeDef = TypedDict(
    "TsvStoreOptionsTypeDef",
    {
        "annotationType": AnnotationTypeType,
        "formatToHeader": Dict[FormatToHeaderKeyType, str],
        "schema": List[Dict[str, SchemaValueTypeType]],
    },
    total=False,
)

TsvVersionOptionsTypeDef = TypedDict(
    "TsvVersionOptionsTypeDef",
    {
        "annotationType": AnnotationTypeType,
        "formatToHeader": Dict[FormatToHeaderKeyType, str],
        "schema": List[Dict[str, SchemaValueTypeType]],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnnotationStoreRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateAnnotationStoreRequestRequestTypeDef(
    _RequiredUpdateAnnotationStoreRequestRequestTypeDef,
    _OptionalUpdateAnnotationStoreRequestRequestTypeDef,
):
    pass

UpdateAnnotationStoreResponseTypeDef = TypedDict(
    "UpdateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "storeOptions": "StoreOptionsTypeDef",
        "storeFormat": StoreFormatType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
    },
)
_OptionalUpdateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateAnnotationStoreVersionRequestRequestTypeDef(
    _RequiredUpdateAnnotationStoreVersionRequestRequestTypeDef,
    _OptionalUpdateAnnotationStoreVersionRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRunGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRunGroupRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateRunGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRunGroupRequestRequestTypeDef",
    {
        "name": str,
        "maxCpus": int,
        "maxRuns": int,
        "maxDuration": int,
        "maxGpus": int,
    },
    total=False,
)

class UpdateRunGroupRequestRequestTypeDef(
    _RequiredUpdateRunGroupRequestRequestTypeDef, _OptionalUpdateRunGroupRequestRequestTypeDef
):
    pass

_RequiredUpdateVariantStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVariantStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateVariantStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVariantStoreRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateVariantStoreRequestRequestTypeDef(
    _RequiredUpdateVariantStoreRequestRequestTypeDef,
    _OptionalUpdateVariantStoreRequestRequestTypeDef,
):
    pass

UpdateVariantStoreResponseTypeDef = TypedDict(
    "UpdateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkflowRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateWorkflowRequestRequestTypeDef(
    _RequiredUpdateWorkflowRequestRequestTypeDef, _OptionalUpdateWorkflowRequestRequestTypeDef
):
    pass

UploadReadSetPartRequestRequestTypeDef = TypedDict(
    "UploadReadSetPartRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "partNumber": int,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)

UploadReadSetPartResponseTypeDef = TypedDict(
    "UploadReadSetPartResponseTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVariantImportItemDetailTypeDef = TypedDict(
    "_RequiredVariantImportItemDetailTypeDef",
    {
        "source": str,
        "jobStatus": JobStatusType,
    },
)
_OptionalVariantImportItemDetailTypeDef = TypedDict(
    "_OptionalVariantImportItemDetailTypeDef",
    {
        "statusMessage": str,
    },
    total=False,
)

class VariantImportItemDetailTypeDef(
    _RequiredVariantImportItemDetailTypeDef, _OptionalVariantImportItemDetailTypeDef
):
    pass

VariantImportItemSourceTypeDef = TypedDict(
    "VariantImportItemSourceTypeDef",
    {
        "source": str,
    },
)

_RequiredVariantImportJobItemTypeDef = TypedDict(
    "_RequiredVariantImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalVariantImportJobItemTypeDef = TypedDict(
    "_OptionalVariantImportJobItemTypeDef",
    {
        "completionTime": datetime,
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
    },
    total=False,
)

class VariantImportJobItemTypeDef(
    _RequiredVariantImportJobItemTypeDef, _OptionalVariantImportJobItemTypeDef
):
    pass

VariantStoreItemTypeDef = TypedDict(
    "VariantStoreItemTypeDef",
    {
        "id": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
    },
)

VcfOptionsTypeDef = TypedDict(
    "VcfOptionsTypeDef",
    {
        "ignoreQualField": bool,
        "ignoreFilterField": bool,
    },
    total=False,
)

VersionDeleteErrorTypeDef = TypedDict(
    "VersionDeleteErrorTypeDef",
    {
        "versionName": str,
        "message": str,
    },
)

VersionOptionsTypeDef = TypedDict(
    "VersionOptionsTypeDef",
    {
        "tsvVersionOptions": "TsvVersionOptionsTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WorkflowListItemTypeDef = TypedDict(
    "WorkflowListItemTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": WorkflowStatusType,
        "type": WorkflowTypeType,
        "digest": str,
        "creationTime": datetime,
        "metadata": Dict[str, str],
    },
    total=False,
)

WorkflowParameterTypeDef = TypedDict(
    "WorkflowParameterTypeDef",
    {
        "description": str,
        "optional": bool,
    },
    total=False,
)
