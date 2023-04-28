"""
Type annotations for omics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_omics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_omics.type_defs import ActivateReadSetFilterTypeDef

    data: ActivateReadSetFilterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AnnotationTypeType,
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
    ReadSetStatusType,
    ReferenceFileType,
    ReferenceImportJobItemStatusType,
    ReferenceImportJobStatusType,
    ReferenceStatusType,
    RunLogLevelType,
    RunStatusType,
    SchemaValueTypeType,
    StoreFormatType,
    StoreStatusType,
    TaskStatusType,
    WorkflowEngineType,
    WorkflowStatusType,
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
    "ActivateReadSetFilterTypeDef",
    "ActivateReadSetJobItemTypeDef",
    "ActivateReadSetSourceItemTypeDef",
    "AnnotationImportItemDetailTypeDef",
    "AnnotationImportItemSourceTypeDef",
    "AnnotationImportJobItemTypeDef",
    "AnnotationStoreItemTypeDef",
    "BatchDeleteReadSetRequestRequestTypeDef",
    "BatchDeleteReadSetResponseTypeDef",
    "CancelAnnotationImportRequestRequestTypeDef",
    "CancelRunRequestRequestTypeDef",
    "CancelVariantImportRequestRequestTypeDef",
    "CreateAnnotationStoreRequestRequestTypeDef",
    "CreateAnnotationStoreResponseTypeDef",
    "CreateReferenceStoreRequestRequestTypeDef",
    "CreateReferenceStoreResponseTypeDef",
    "CreateRunGroupRequestRequestTypeDef",
    "CreateRunGroupResponseTypeDef",
    "CreateSequenceStoreRequestRequestTypeDef",
    "CreateSequenceStoreResponseTypeDef",
    "CreateVariantStoreRequestRequestTypeDef",
    "CreateVariantStoreResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DeleteAnnotationStoreRequestRequestTypeDef",
    "DeleteAnnotationStoreResponseTypeDef",
    "DeleteReferenceRequestRequestTypeDef",
    "DeleteReferenceStoreRequestRequestTypeDef",
    "DeleteRunGroupRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteSequenceStoreRequestRequestTypeDef",
    "DeleteVariantStoreRequestRequestTypeDef",
    "DeleteVariantStoreResponseTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "ExportReadSetDetailTypeDef",
    "ExportReadSetFilterTypeDef",
    "ExportReadSetJobDetailTypeDef",
    "ExportReadSetTypeDef",
    "FileInformationTypeDef",
    "FormatOptionsTypeDef",
    "GetAnnotationImportRequestRequestTypeDef",
    "GetAnnotationImportResponseTypeDef",
    "GetAnnotationStoreRequestRequestTypeDef",
    "GetAnnotationStoreResponseTypeDef",
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
    "ListAnnotationStoresFilterTypeDef",
    "ListAnnotationStoresRequestRequestTypeDef",
    "ListAnnotationStoresResponseTypeDef",
    "ListReadSetActivationJobsRequestRequestTypeDef",
    "ListReadSetActivationJobsResponseTypeDef",
    "ListReadSetExportJobsRequestRequestTypeDef",
    "ListReadSetExportJobsResponseTypeDef",
    "ListReadSetImportJobsRequestRequestTypeDef",
    "ListReadSetImportJobsResponseTypeDef",
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
    "PaginatorConfigTypeDef",
    "ReadOptionsTypeDef",
    "ReadSetBatchErrorTypeDef",
    "ReadSetFilesTypeDef",
    "ReadSetFilterTypeDef",
    "ReadSetListItemTypeDef",
    "ReferenceFilesTypeDef",
    "ReferenceFilterTypeDef",
    "ReferenceItemTypeDef",
    "ReferenceListItemTypeDef",
    "ReferenceStoreDetailTypeDef",
    "ReferenceStoreFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RunGroupListItemTypeDef",
    "RunListItemTypeDef",
    "SequenceInformationTypeDef",
    "SequenceStoreDetailTypeDef",
    "SequenceStoreFilterTypeDef",
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
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnnotationStoreRequestRequestTypeDef",
    "UpdateAnnotationStoreResponseTypeDef",
    "UpdateRunGroupRequestRequestTypeDef",
    "UpdateVariantStoreRequestRequestTypeDef",
    "UpdateVariantStoreResponseTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "VariantImportItemDetailTypeDef",
    "VariantImportItemSourceTypeDef",
    "VariantImportJobItemTypeDef",
    "VariantStoreItemTypeDef",
    "VcfOptionsTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowListItemTypeDef",
    "WorkflowParameterTypeDef",
)

ActivateReadSetFilterTypeDef = TypedDict(
    "ActivateReadSetFilterTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "status": ReadSetActivationJobStatusType,
    },
    total=False,
)

_RequiredActivateReadSetJobItemTypeDef = TypedDict(
    "_RequiredActivateReadSetJobItemTypeDef",
    {
        "creationTime": datetime,
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
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
        "jobStatus": JobStatusType,
        "source": str,
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
        "creationTime": datetime,
        "destinationName": str,
        "id": str,
        "roleArn": str,
        "status": JobStatusType,
        "updateTime": datetime,
    },
)
_OptionalAnnotationImportJobItemTypeDef = TypedDict(
    "_OptionalAnnotationImportJobItemTypeDef",
    {
        "completionTime": datetime,
        "runLeftNormalization": bool,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "sseConfig": "SseConfigTypeDef",
        "status": StoreStatusType,
        "statusMessage": str,
        "storeArn": str,
        "storeFormat": StoreFormatType,
        "storeSizeBytes": int,
        "updateTime": datetime,
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

_RequiredCreateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnnotationStoreRequestRequestTypeDef",
    {
        "storeFormat": StoreFormatType,
    },
)
_OptionalCreateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnnotationStoreRequestRequestTypeDef",
    {
        "description": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "sseConfig": "SseConfigTypeDef",
        "storeOptions": "StoreOptionsTypeDef",
        "tags": Dict[str, str],
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
        "creationTime": datetime,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeFormat": StoreFormatType,
        "storeOptions": "StoreOptionsTypeDef",
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
        "clientToken": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "tags": Dict[str, str],
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
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
        "maxCpus": int,
        "maxDuration": int,
        "maxRuns": int,
        "name": str,
        "tags": Dict[str, str],
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
        "clientToken": str,
        "description": str,
        "sseConfig": "SseConfigTypeDef",
        "tags": Dict[str, str],
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
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
        "description": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
        "tags": Dict[str, str],
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
        "creationTime": datetime,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
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
        "definitionUri": str,
        "definitionZip": Union[bytes, IO[bytes], StreamingBody],
        "description": str,
        "engine": WorkflowEngineType,
        "main": str,
        "name": str,
        "parameterTemplate": Dict[str, "WorkflowParameterTypeDef"],
        "storageCapacity": int,
        "tags": Dict[str, str],
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
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "status": ReadSetExportJobStatusType,
    },
    total=False,
)

_RequiredExportReadSetJobDetailTypeDef = TypedDict(
    "_RequiredExportReadSetJobDetailTypeDef",
    {
        "creationTime": datetime,
        "destination": str,
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetExportJobStatusType,
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
        "contentLength": int,
        "partSize": int,
        "totalParts": int,
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
        "completionTime": datetime,
        "creationTime": datetime,
        "destinationName": str,
        "formatOptions": "FormatOptionsTypeDef",
        "id": str,
        "items": List["AnnotationImportItemDetailTypeDef"],
        "roleArn": str,
        "runLeftNormalization": bool,
        "status": JobStatusType,
        "statusMessage": str,
        "updateTime": datetime,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "sseConfig": "SseConfigTypeDef",
        "status": StoreStatusType,
        "statusMessage": str,
        "storeArn": str,
        "storeFormat": StoreFormatType,
        "storeOptions": "StoreOptionsTypeDef",
        "storeSizeBytes": int,
        "tags": Dict[str, str],
        "updateTime": datetime,
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
        "completionTime": datetime,
        "creationTime": datetime,
        "id": str,
        "sequenceStoreId": str,
        "sources": List["ActivateReadSetSourceItemTypeDef"],
        "status": ReadSetActivationJobStatusType,
        "statusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReadSetExportJobRequestRequestTypeDef = TypedDict(
    "GetReadSetExportJobRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)

GetReadSetExportJobResponseTypeDef = TypedDict(
    "GetReadSetExportJobResponseTypeDef",
    {
        "completionTime": datetime,
        "creationTime": datetime,
        "destination": str,
        "id": str,
        "readSets": List["ExportReadSetDetailTypeDef"],
        "sequenceStoreId": str,
        "status": ReadSetExportJobStatusType,
        "statusMessage": str,
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
        "completionTime": datetime,
        "creationTime": datetime,
        "id": str,
        "roleArn": str,
        "sequenceStoreId": str,
        "sources": List["ImportReadSetSourceItemTypeDef"],
        "status": ReadSetImportJobStatusType,
        "statusMessage": str,
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "fileType": FileTypeType,
        "files": "ReadSetFilesTypeDef",
        "id": str,
        "name": str,
        "referenceArn": str,
        "sampleId": str,
        "sequenceInformation": "SequenceInformationTypeDef",
        "sequenceStoreId": str,
        "status": ReadSetStatusType,
        "subjectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReadSetRequestRequestTypeDef = TypedDict(
    "_RequiredGetReadSetRequestRequestTypeDef",
    {
        "id": str,
        "partNumber": int,
        "sequenceStoreId": str,
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
        "completionTime": datetime,
        "creationTime": datetime,
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "sources": List["ImportReferenceSourceItemTypeDef"],
        "status": ReferenceImportJobStatusType,
        "statusMessage": str,
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "files": "ReferenceFilesTypeDef",
        "id": str,
        "md5": str,
        "name": str,
        "referenceStoreId": str,
        "status": ReferenceStatusType,
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReferenceRequestRequestTypeDef = TypedDict(
    "_RequiredGetReferenceRequestRequestTypeDef",
    {
        "id": str,
        "partNumber": int,
        "referenceStoreId": str,
    },
)
_OptionalGetReferenceRequestRequestTypeDef = TypedDict(
    "_OptionalGetReferenceRequestRequestTypeDef",
    {
        "file": ReferenceFileType,
        "range": str,
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
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
        "creationTime": datetime,
        "id": str,
        "maxCpus": int,
        "maxDuration": int,
        "maxRuns": int,
        "name": str,
        "tags": Dict[str, str],
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
        "creationTime": datetime,
        "definition": str,
        "digest": str,
        "id": str,
        "logLevel": RunLogLevelType,
        "name": str,
        "outputUri": str,
        "parameters": Dict[str, Any],
        "priority": int,
        "resourceDigests": Dict[str, str],
        "roleArn": str,
        "runGroupId": str,
        "runId": str,
        "startTime": datetime,
        "startedBy": str,
        "status": RunStatusType,
        "statusMessage": str,
        "stopTime": datetime,
        "storageCapacity": int,
        "tags": Dict[str, str],
        "workflowId": str,
        "workflowType": Literal["PRIVATE"],
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
        "cpus": int,
        "creationTime": datetime,
        "logStream": str,
        "memory": int,
        "name": str,
        "startTime": datetime,
        "status": TaskStatusType,
        "statusMessage": str,
        "stopTime": datetime,
        "taskId": str,
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
        "arn": str,
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
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
        "completionTime": datetime,
        "creationTime": datetime,
        "destinationName": str,
        "id": str,
        "items": List["VariantImportItemDetailTypeDef"],
        "roleArn": str,
        "runLeftNormalization": bool,
        "status": JobStatusType,
        "statusMessage": str,
        "updateTime": datetime,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "sseConfig": "SseConfigTypeDef",
        "status": StoreStatusType,
        "statusMessage": str,
        "storeArn": str,
        "storeSizeBytes": int,
        "tags": Dict[str, str],
        "updateTime": datetime,
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
        "export": List[Literal["DEFINITION"]],
        "type": Literal["PRIVATE"],
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
        "creationTime": datetime,
        "definition": str,
        "description": str,
        "digest": str,
        "engine": WorkflowEngineType,
        "id": str,
        "main": str,
        "name": str,
        "parameterTemplate": Dict[str, "WorkflowParameterTypeDef"],
        "status": WorkflowStatusType,
        "statusMessage": str,
        "storageCapacity": int,
        "tags": Dict[str, str],
        "type": Literal["PRIVATE"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportReadSetFilterTypeDef = TypedDict(
    "ImportReadSetFilterTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "status": ReadSetImportJobStatusType,
    },
    total=False,
)

_RequiredImportReadSetJobItemTypeDef = TypedDict(
    "_RequiredImportReadSetJobItemTypeDef",
    {
        "creationTime": datetime,
        "id": str,
        "roleArn": str,
        "sequenceStoreId": str,
        "status": ReadSetImportJobStatusType,
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
        "sampleId": str,
        "sourceFileType": FileTypeType,
        "sourceFiles": "SourceFilesTypeDef",
        "status": ReadSetImportJobItemStatusType,
        "subjectId": str,
    },
)
_OptionalImportReadSetSourceItemTypeDef = TypedDict(
    "_OptionalImportReadSetSourceItemTypeDef",
    {
        "description": str,
        "generatedFrom": str,
        "name": str,
        "referenceArn": str,
        "statusMessage": str,
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
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "status": ReferenceImportJobStatusType,
    },
    total=False,
)

_RequiredImportReferenceJobItemTypeDef = TypedDict(
    "_RequiredImportReferenceJobItemTypeDef",
    {
        "creationTime": datetime,
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
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
        "description": str,
        "name": str,
        "sourceFile": str,
        "statusMessage": str,
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
        "filter": "ListAnnotationImportJobsFilterTypeDef",
        "ids": List[str],
        "maxResults": int,
        "nextToken": str,
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
        "filter": "ListAnnotationStoresFilterTypeDef",
        "ids": List[str],
        "maxResults": int,
        "nextToken": str,
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

_RequiredListReadSetActivationJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListReadSetActivationJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
    },
)
_OptionalListReadSetActivationJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListReadSetActivationJobsRequestRequestTypeDef",
    {
        "filter": "ActivateReadSetFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "activationJobs": List["ActivateReadSetJobItemTypeDef"],
        "nextToken": str,
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
        "filter": "ExportReadSetFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "exportJobs": List["ExportReadSetJobDetailTypeDef"],
        "nextToken": str,
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
        "filter": "ImportReadSetFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "importJobs": List["ImportReadSetJobItemTypeDef"],
        "nextToken": str,
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
        "filter": "ReadSetFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "filter": "ImportReferenceFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "importJobs": List["ImportReferenceJobItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReferenceStoresRequestRequestTypeDef = TypedDict(
    "ListReferenceStoresRequestRequestTypeDef",
    {
        "filter": "ReferenceStoreFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "filter": "ReferenceFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "maxResults": int,
        "name": str,
        "startingToken": str,
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
        "maxResults": int,
        "startingToken": str,
        "status": TaskStatusType,
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
        "maxResults": int,
        "name": str,
        "runGroupId": str,
        "startingToken": str,
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
        "filter": "SequenceStoreFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
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
        "filter": "ListVariantImportJobsFilterTypeDef",
        "ids": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVariantImportJobsResponseTypeDef = TypedDict(
    "ListVariantImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "variantImportJobs": List["VariantImportJobItemTypeDef"],
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
        "filter": "ListVariantStoresFilterTypeDef",
        "ids": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVariantStoresResponseTypeDef = TypedDict(
    "ListVariantStoresResponseTypeDef",
    {
        "nextToken": str,
        "variantStores": List["VariantStoreItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "maxResults": int,
        "name": str,
        "startingToken": str,
        "type": Literal["PRIVATE"],
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
        "comment": str,
        "encoding": str,
        "escape": str,
        "escapeQuotes": bool,
        "header": bool,
        "lineSep": str,
        "quote": str,
        "quoteAll": bool,
        "sep": str,
    },
    total=False,
)

ReadSetBatchErrorTypeDef = TypedDict(
    "ReadSetBatchErrorTypeDef",
    {
        "code": str,
        "id": str,
        "message": str,
    },
)

ReadSetFilesTypeDef = TypedDict(
    "ReadSetFilesTypeDef",
    {
        "index": "FileInformationTypeDef",
        "source1": "FileInformationTypeDef",
        "source2": "FileInformationTypeDef",
    },
    total=False,
)

ReadSetFilterTypeDef = TypedDict(
    "ReadSetFilterTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "name": str,
        "referenceArn": str,
        "status": ReadSetStatusType,
    },
    total=False,
)

_RequiredReadSetListItemTypeDef = TypedDict(
    "_RequiredReadSetListItemTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "fileType": FileTypeType,
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetStatusType,
    },
)
_OptionalReadSetListItemTypeDef = TypedDict(
    "_OptionalReadSetListItemTypeDef",
    {
        "description": str,
        "name": str,
        "referenceArn": str,
        "sampleId": str,
        "sequenceInformation": "SequenceInformationTypeDef",
        "subjectId": str,
    },
    total=False,
)

class ReadSetListItemTypeDef(_RequiredReadSetListItemTypeDef, _OptionalReadSetListItemTypeDef):
    pass

ReferenceFilesTypeDef = TypedDict(
    "ReferenceFilesTypeDef",
    {
        "index": "FileInformationTypeDef",
        "source": "FileInformationTypeDef",
    },
    total=False,
)

ReferenceFilterTypeDef = TypedDict(
    "ReferenceFilterTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "md5": str,
        "name": str,
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
        "arn": str,
        "creationTime": datetime,
        "id": str,
        "md5": str,
        "referenceStoreId": str,
        "updateTime": datetime,
    },
)
_OptionalReferenceListItemTypeDef = TypedDict(
    "_OptionalReferenceListItemTypeDef",
    {
        "description": str,
        "name": str,
        "status": ReferenceStatusType,
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
        "creationTime": datetime,
        "id": str,
    },
)
_OptionalReferenceStoreDetailTypeDef = TypedDict(
    "_OptionalReferenceStoreDetailTypeDef",
    {
        "description": str,
        "name": str,
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
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "name": str,
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
        "creationTime": datetime,
        "id": str,
        "maxCpus": int,
        "maxDuration": int,
        "maxRuns": int,
        "name": str,
    },
    total=False,
)

RunListItemTypeDef = TypedDict(
    "RunListItemTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "id": str,
        "name": str,
        "priority": int,
        "startTime": datetime,
        "status": RunStatusType,
        "stopTime": datetime,
        "storageCapacity": int,
        "workflowId": str,
    },
    total=False,
)

SequenceInformationTypeDef = TypedDict(
    "SequenceInformationTypeDef",
    {
        "alignment": str,
        "generatedFrom": str,
        "totalBaseCount": int,
        "totalReadCount": int,
    },
    total=False,
)

_RequiredSequenceStoreDetailTypeDef = TypedDict(
    "_RequiredSequenceStoreDetailTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "id": str,
    },
)
_OptionalSequenceStoreDetailTypeDef = TypedDict(
    "_OptionalSequenceStoreDetailTypeDef",
    {
        "description": str,
        "name": str,
        "sseConfig": "SseConfigTypeDef",
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
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "name": str,
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
        "items": List["AnnotationImportItemSourceTypeDef"],
        "roleArn": str,
    },
)
_OptionalStartAnnotationImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartAnnotationImportRequestRequestTypeDef",
    {
        "formatOptions": "FormatOptionsTypeDef",
        "runLeftNormalization": bool,
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
        "creationTime": datetime,
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
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
        "destination": str,
        "roleArn": str,
        "sequenceStoreId": str,
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
        "creationTime": datetime,
        "destination": str,
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetExportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReadSetImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartReadSetImportJobRequestRequestTypeDef",
    {
        "roleArn": str,
        "sequenceStoreId": str,
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
        "creationTime": datetime,
        "id": str,
        "roleArn": str,
        "sequenceStoreId": str,
        "status": ReadSetImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReadSetImportJobSourceItemTypeDef = TypedDict(
    "_RequiredStartReadSetImportJobSourceItemTypeDef",
    {
        "referenceArn": str,
        "sampleId": str,
        "sourceFileType": FileTypeType,
        "sourceFiles": "SourceFilesTypeDef",
        "subjectId": str,
    },
)
_OptionalStartReadSetImportJobSourceItemTypeDef = TypedDict(
    "_OptionalStartReadSetImportJobSourceItemTypeDef",
    {
        "description": str,
        "generatedFrom": str,
        "name": str,
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
        "creationTime": datetime,
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReferenceImportJobSourceItemTypeDef = TypedDict(
    "_RequiredStartReferenceImportJobSourceItemTypeDef",
    {
        "name": str,
        "sourceFile": str,
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
        "requestId": str,
        "roleArn": str,
    },
)
_OptionalStartRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartRunRequestRequestTypeDef",
    {
        "logLevel": RunLogLevelType,
        "name": str,
        "outputUri": str,
        "parameters": Dict[str, Any],
        "priority": int,
        "runGroupId": str,
        "runId": str,
        "storageCapacity": int,
        "tags": Dict[str, str],
        "workflowId": str,
        "workflowType": Literal["PRIVATE"],
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVariantImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartVariantImportRequestRequestTypeDef",
    {
        "destinationName": str,
        "items": List["VariantImportItemSourceTypeDef"],
        "roleArn": str,
    },
)
_OptionalStartVariantImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartVariantImportRequestRequestTypeDef",
    {
        "runLeftNormalization": bool,
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
        "cpus": int,
        "creationTime": datetime,
        "memory": int,
        "name": str,
        "startTime": datetime,
        "status": TaskStatusType,
        "stopTime": datetime,
        "taskId": str,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
        "storeFormat": StoreFormatType,
        "storeOptions": "StoreOptionsTypeDef",
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
        "maxCpus": int,
        "maxDuration": int,
        "maxRuns": int,
        "name": str,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "status": StoreStatusType,
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
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateWorkflowRequestRequestTypeDef(
    _RequiredUpdateWorkflowRequestRequestTypeDef, _OptionalUpdateWorkflowRequestRequestTypeDef
):
    pass

_RequiredVariantImportItemDetailTypeDef = TypedDict(
    "_RequiredVariantImportItemDetailTypeDef",
    {
        "jobStatus": JobStatusType,
        "source": str,
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
        "creationTime": datetime,
        "destinationName": str,
        "id": str,
        "roleArn": str,
        "status": JobStatusType,
        "updateTime": datetime,
    },
)
_OptionalVariantImportJobItemTypeDef = TypedDict(
    "_OptionalVariantImportJobItemTypeDef",
    {
        "completionTime": datetime,
        "runLeftNormalization": bool,
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
        "creationTime": datetime,
        "description": str,
        "id": str,
        "name": str,
        "reference": "ReferenceItemTypeDef",
        "sseConfig": "SseConfigTypeDef",
        "status": StoreStatusType,
        "statusMessage": str,
        "storeArn": str,
        "storeSizeBytes": int,
        "updateTime": datetime,
    },
)

VcfOptionsTypeDef = TypedDict(
    "VcfOptionsTypeDef",
    {
        "ignoreFilterField": bool,
        "ignoreQualField": bool,
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
        "creationTime": datetime,
        "digest": str,
        "id": str,
        "name": str,
        "status": WorkflowStatusType,
        "type": Literal["PRIVATE"],
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
