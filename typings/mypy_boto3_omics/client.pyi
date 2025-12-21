"""
Type annotations for omics service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_omics.client import OmicsClient

    session = Session()
    client: OmicsClient = session.client("omics")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAnnotationImportJobsPaginator,
    ListAnnotationStoresPaginator,
    ListAnnotationStoreVersionsPaginator,
    ListMultipartReadSetUploadsPaginator,
    ListReadSetActivationJobsPaginator,
    ListReadSetExportJobsPaginator,
    ListReadSetImportJobsPaginator,
    ListReadSetsPaginator,
    ListReadSetUploadPartsPaginator,
    ListReferenceImportJobsPaginator,
    ListReferencesPaginator,
    ListReferenceStoresPaginator,
    ListRunCachesPaginator,
    ListRunGroupsPaginator,
    ListRunsPaginator,
    ListRunTasksPaginator,
    ListSequenceStoresPaginator,
    ListSharesPaginator,
    ListVariantImportJobsPaginator,
    ListVariantStoresPaginator,
    ListWorkflowsPaginator,
    ListWorkflowVersionsPaginator,
)
from .type_defs import (
    AbortMultipartReadSetUploadRequestTypeDef,
    AcceptShareRequestTypeDef,
    AcceptShareResponseTypeDef,
    BatchDeleteReadSetRequestTypeDef,
    BatchDeleteReadSetResponseTypeDef,
    CancelAnnotationImportRequestTypeDef,
    CancelRunRequestTypeDef,
    CancelVariantImportRequestTypeDef,
    CompleteMultipartReadSetUploadRequestTypeDef,
    CompleteMultipartReadSetUploadResponseTypeDef,
    CreateAnnotationStoreRequestTypeDef,
    CreateAnnotationStoreResponseTypeDef,
    CreateAnnotationStoreVersionRequestTypeDef,
    CreateAnnotationStoreVersionResponseTypeDef,
    CreateMultipartReadSetUploadRequestTypeDef,
    CreateMultipartReadSetUploadResponseTypeDef,
    CreateReferenceStoreRequestTypeDef,
    CreateReferenceStoreResponseTypeDef,
    CreateRunCacheRequestTypeDef,
    CreateRunCacheResponseTypeDef,
    CreateRunGroupRequestTypeDef,
    CreateRunGroupResponseTypeDef,
    CreateSequenceStoreRequestTypeDef,
    CreateSequenceStoreResponseTypeDef,
    CreateShareRequestTypeDef,
    CreateShareResponseTypeDef,
    CreateVariantStoreRequestTypeDef,
    CreateVariantStoreResponseTypeDef,
    CreateWorkflowRequestTypeDef,
    CreateWorkflowResponseTypeDef,
    CreateWorkflowVersionRequestTypeDef,
    CreateWorkflowVersionResponseTypeDef,
    DeleteAnnotationStoreRequestTypeDef,
    DeleteAnnotationStoreResponseTypeDef,
    DeleteAnnotationStoreVersionsRequestTypeDef,
    DeleteAnnotationStoreVersionsResponseTypeDef,
    DeleteReferenceRequestTypeDef,
    DeleteReferenceStoreRequestTypeDef,
    DeleteRunCacheRequestTypeDef,
    DeleteRunGroupRequestTypeDef,
    DeleteRunRequestTypeDef,
    DeleteS3AccessPolicyRequestTypeDef,
    DeleteSequenceStoreRequestTypeDef,
    DeleteShareRequestTypeDef,
    DeleteShareResponseTypeDef,
    DeleteVariantStoreRequestTypeDef,
    DeleteVariantStoreResponseTypeDef,
    DeleteWorkflowRequestTypeDef,
    DeleteWorkflowVersionRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAnnotationImportRequestTypeDef,
    GetAnnotationImportResponseTypeDef,
    GetAnnotationStoreRequestTypeDef,
    GetAnnotationStoreResponseTypeDef,
    GetAnnotationStoreVersionRequestTypeDef,
    GetAnnotationStoreVersionResponseTypeDef,
    GetReadSetActivationJobRequestTypeDef,
    GetReadSetActivationJobResponseTypeDef,
    GetReadSetExportJobRequestTypeDef,
    GetReadSetExportJobResponseTypeDef,
    GetReadSetImportJobRequestTypeDef,
    GetReadSetImportJobResponseTypeDef,
    GetReadSetMetadataRequestTypeDef,
    GetReadSetMetadataResponseTypeDef,
    GetReadSetRequestTypeDef,
    GetReadSetResponseTypeDef,
    GetReferenceImportJobRequestTypeDef,
    GetReferenceImportJobResponseTypeDef,
    GetReferenceMetadataRequestTypeDef,
    GetReferenceMetadataResponseTypeDef,
    GetReferenceRequestTypeDef,
    GetReferenceResponseTypeDef,
    GetReferenceStoreRequestTypeDef,
    GetReferenceStoreResponseTypeDef,
    GetRunCacheRequestTypeDef,
    GetRunCacheResponseTypeDef,
    GetRunGroupRequestTypeDef,
    GetRunGroupResponseTypeDef,
    GetRunRequestTypeDef,
    GetRunResponseTypeDef,
    GetRunTaskRequestTypeDef,
    GetRunTaskResponseTypeDef,
    GetS3AccessPolicyRequestTypeDef,
    GetS3AccessPolicyResponseTypeDef,
    GetSequenceStoreRequestTypeDef,
    GetSequenceStoreResponseTypeDef,
    GetShareRequestTypeDef,
    GetShareResponseTypeDef,
    GetVariantImportRequestTypeDef,
    GetVariantImportResponseTypeDef,
    GetVariantStoreRequestTypeDef,
    GetVariantStoreResponseTypeDef,
    GetWorkflowRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowVersionRequestTypeDef,
    GetWorkflowVersionResponseTypeDef,
    ListAnnotationImportJobsRequestTypeDef,
    ListAnnotationImportJobsResponseTypeDef,
    ListAnnotationStoresRequestTypeDef,
    ListAnnotationStoresResponseTypeDef,
    ListAnnotationStoreVersionsRequestTypeDef,
    ListAnnotationStoreVersionsResponseTypeDef,
    ListMultipartReadSetUploadsRequestTypeDef,
    ListMultipartReadSetUploadsResponseTypeDef,
    ListReadSetActivationJobsRequestTypeDef,
    ListReadSetActivationJobsResponseTypeDef,
    ListReadSetExportJobsRequestTypeDef,
    ListReadSetExportJobsResponseTypeDef,
    ListReadSetImportJobsRequestTypeDef,
    ListReadSetImportJobsResponseTypeDef,
    ListReadSetsRequestTypeDef,
    ListReadSetsResponseTypeDef,
    ListReadSetUploadPartsRequestTypeDef,
    ListReadSetUploadPartsResponseTypeDef,
    ListReferenceImportJobsRequestTypeDef,
    ListReferenceImportJobsResponseTypeDef,
    ListReferencesRequestTypeDef,
    ListReferencesResponseTypeDef,
    ListReferenceStoresRequestTypeDef,
    ListReferenceStoresResponseTypeDef,
    ListRunCachesRequestTypeDef,
    ListRunCachesResponseTypeDef,
    ListRunGroupsRequestTypeDef,
    ListRunGroupsResponseTypeDef,
    ListRunsRequestTypeDef,
    ListRunsResponseTypeDef,
    ListRunTasksRequestTypeDef,
    ListRunTasksResponseTypeDef,
    ListSequenceStoresRequestTypeDef,
    ListSequenceStoresResponseTypeDef,
    ListSharesRequestTypeDef,
    ListSharesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVariantImportJobsRequestTypeDef,
    ListVariantImportJobsResponseTypeDef,
    ListVariantStoresRequestTypeDef,
    ListVariantStoresResponseTypeDef,
    ListWorkflowsRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    ListWorkflowVersionsRequestTypeDef,
    ListWorkflowVersionsResponseTypeDef,
    PutS3AccessPolicyRequestTypeDef,
    PutS3AccessPolicyResponseTypeDef,
    StartAnnotationImportRequestTypeDef,
    StartAnnotationImportResponseTypeDef,
    StartReadSetActivationJobRequestTypeDef,
    StartReadSetActivationJobResponseTypeDef,
    StartReadSetExportJobRequestTypeDef,
    StartReadSetExportJobResponseTypeDef,
    StartReadSetImportJobRequestTypeDef,
    StartReadSetImportJobResponseTypeDef,
    StartReferenceImportJobRequestTypeDef,
    StartReferenceImportJobResponseTypeDef,
    StartRunRequestTypeDef,
    StartRunResponseTypeDef,
    StartVariantImportRequestTypeDef,
    StartVariantImportResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAnnotationStoreRequestTypeDef,
    UpdateAnnotationStoreResponseTypeDef,
    UpdateAnnotationStoreVersionRequestTypeDef,
    UpdateAnnotationStoreVersionResponseTypeDef,
    UpdateRunCacheRequestTypeDef,
    UpdateRunGroupRequestTypeDef,
    UpdateSequenceStoreRequestTypeDef,
    UpdateSequenceStoreResponseTypeDef,
    UpdateVariantStoreRequestTypeDef,
    UpdateVariantStoreResponseTypeDef,
    UpdateWorkflowRequestTypeDef,
    UpdateWorkflowVersionRequestTypeDef,
    UploadReadSetPartRequestTypeDef,
    UploadReadSetPartResponseTypeDef,
)
from .waiter import (
    AnnotationImportJobCreatedWaiter,
    AnnotationStoreCreatedWaiter,
    AnnotationStoreDeletedWaiter,
    AnnotationStoreVersionCreatedWaiter,
    AnnotationStoreVersionDeletedWaiter,
    ReadSetActivationJobCompletedWaiter,
    ReadSetExportJobCompletedWaiter,
    ReadSetImportJobCompletedWaiter,
    ReferenceImportJobCompletedWaiter,
    RunCompletedWaiter,
    RunRunningWaiter,
    TaskCompletedWaiter,
    TaskRunningWaiter,
    VariantImportJobCreatedWaiter,
    VariantStoreCreatedWaiter,
    VariantStoreDeletedWaiter,
    WorkflowActiveWaiter,
    WorkflowVersionActiveWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("OmicsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotSupportedOperationException: Type[BotocoreClientError]
    RangeNotSatisfiableException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OmicsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OmicsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#generate_presigned_url)
        """

    def abort_multipart_read_set_upload(
        self, **kwargs: Unpack[AbortMultipartReadSetUploadRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a multipart read set upload into a sequence store and returns a response
        with no body if the operation is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/abort_multipart_read_set_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#abort_multipart_read_set_upload)
        """

    def accept_share(
        self, **kwargs: Unpack[AcceptShareRequestTypeDef]
    ) -> AcceptShareResponseTypeDef:
        """
        Accept a resource share request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/accept_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#accept_share)
        """

    def batch_delete_read_set(
        self, **kwargs: Unpack[BatchDeleteReadSetRequestTypeDef]
    ) -> BatchDeleteReadSetResponseTypeDef:
        """
        Deletes one or more read sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/batch_delete_read_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#batch_delete_read_set)
        """

    def cancel_annotation_import_job(
        self, **kwargs: Unpack[CancelAnnotationImportRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/cancel_annotation_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#cancel_annotation_import_job)
        """

    def cancel_run(self, **kwargs: Unpack[CancelRunRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a run using its ID and returns a response with no body if the operation
        is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/cancel_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#cancel_run)
        """

    def cancel_variant_import_job(
        self, **kwargs: Unpack[CancelVariantImportRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/cancel_variant_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#cancel_variant_import_job)
        """

    def complete_multipart_read_set_upload(
        self, **kwargs: Unpack[CompleteMultipartReadSetUploadRequestTypeDef]
    ) -> CompleteMultipartReadSetUploadResponseTypeDef:
        """
        Completes a multipart read set upload into a sequence store after you have
        initiated the upload process with <code>CreateMultipartReadSetUpload</code> and
        uploaded all read set parts using <code>UploadReadSetPart</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/complete_multipart_read_set_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#complete_multipart_read_set_upload)
        """

    def create_annotation_store(
        self, **kwargs: Unpack[CreateAnnotationStoreRequestTypeDef]
    ) -> CreateAnnotationStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_annotation_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_annotation_store)
        """

    def create_annotation_store_version(
        self, **kwargs: Unpack[CreateAnnotationStoreVersionRequestTypeDef]
    ) -> CreateAnnotationStoreVersionResponseTypeDef:
        """
        Creates a new version of an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_annotation_store_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_annotation_store_version)
        """

    def create_multipart_read_set_upload(
        self, **kwargs: Unpack[CreateMultipartReadSetUploadRequestTypeDef]
    ) -> CreateMultipartReadSetUploadResponseTypeDef:
        """
        Initiates a multipart read set upload for uploading partitioned source files
        into a sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_multipart_read_set_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_multipart_read_set_upload)
        """

    def create_reference_store(
        self, **kwargs: Unpack[CreateReferenceStoreRequestTypeDef]
    ) -> CreateReferenceStoreResponseTypeDef:
        """
        Creates a reference store and returns metadata in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_reference_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_reference_store)
        """

    def create_run_cache(
        self, **kwargs: Unpack[CreateRunCacheRequestTypeDef]
    ) -> CreateRunCacheResponseTypeDef:
        """
        Creates a run cache to store and reference task outputs from completed private
        runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_run_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_run_cache)
        """

    def create_run_group(
        self, **kwargs: Unpack[CreateRunGroupRequestTypeDef]
    ) -> CreateRunGroupResponseTypeDef:
        """
        Creates a run group to limit the compute resources for the runs that are added
        to the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_run_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_run_group)
        """

    def create_sequence_store(
        self, **kwargs: Unpack[CreateSequenceStoreRequestTypeDef]
    ) -> CreateSequenceStoreResponseTypeDef:
        """
        Creates a sequence store and returns its metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_sequence_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_sequence_store)
        """

    def create_share(
        self, **kwargs: Unpack[CreateShareRequestTypeDef]
    ) -> CreateShareResponseTypeDef:
        """
        Creates a cross-account shared resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_share)
        """

    def create_variant_store(
        self, **kwargs: Unpack[CreateVariantStoreRequestTypeDef]
    ) -> CreateVariantStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_variant_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_variant_store)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateWorkflowRequestTypeDef]
    ) -> CreateWorkflowResponseTypeDef:
        """
        Creates a private workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_workflow)
        """

    def create_workflow_version(
        self, **kwargs: Unpack[CreateWorkflowVersionRequestTypeDef]
    ) -> CreateWorkflowVersionResponseTypeDef:
        """
        Creates a new workflow version for the workflow that you specify with the
        <code>workflowId</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/create_workflow_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#create_workflow_version)
        """

    def delete_annotation_store(
        self, **kwargs: Unpack[DeleteAnnotationStoreRequestTypeDef]
    ) -> DeleteAnnotationStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_annotation_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_annotation_store)
        """

    def delete_annotation_store_versions(
        self, **kwargs: Unpack[DeleteAnnotationStoreVersionsRequestTypeDef]
    ) -> DeleteAnnotationStoreVersionsResponseTypeDef:
        """
        Deletes one or multiple versions of an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_annotation_store_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_annotation_store_versions)
        """

    def delete_reference(self, **kwargs: Unpack[DeleteReferenceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a reference genome and returns a response with no body if the operation
        is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_reference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_reference)
        """

    def delete_reference_store(
        self, **kwargs: Unpack[DeleteReferenceStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a reference store and returns a response with no body if the operation
        is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_reference_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_reference_store)
        """

    def delete_run(self, **kwargs: Unpack[DeleteRunRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a run and returns a response with no body if the operation is
        successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_run)
        """

    def delete_run_cache(
        self, **kwargs: Unpack[DeleteRunCacheRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a run cache and returns a response with no body if the operation is
        successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_run_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_run_cache)
        """

    def delete_run_group(
        self, **kwargs: Unpack[DeleteRunGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a run group and returns a response with no body if the operation is
        successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_run_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_run_group)
        """

    def delete_s3_access_policy(
        self, **kwargs: Unpack[DeleteS3AccessPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an access policy for the specified store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_s3_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_s3_access_policy)
        """

    def delete_sequence_store(
        self, **kwargs: Unpack[DeleteSequenceStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a sequence store and returns a response with no body if the operation
        is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_sequence_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_sequence_store)
        """

    def delete_share(
        self, **kwargs: Unpack[DeleteShareRequestTypeDef]
    ) -> DeleteShareResponseTypeDef:
        """
        Deletes a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_share)
        """

    def delete_variant_store(
        self, **kwargs: Unpack[DeleteVariantStoreRequestTypeDef]
    ) -> DeleteVariantStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_variant_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_variant_store)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteWorkflowRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a workflow by specifying its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_workflow)
        """

    def delete_workflow_version(
        self, **kwargs: Unpack[DeleteWorkflowVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a workflow version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/delete_workflow_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#delete_workflow_version)
        """

    def get_annotation_import_job(
        self, **kwargs: Unpack[GetAnnotationImportRequestTypeDef]
    ) -> GetAnnotationImportResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_annotation_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_annotation_import_job)
        """

    def get_annotation_store(
        self, **kwargs: Unpack[GetAnnotationStoreRequestTypeDef]
    ) -> GetAnnotationStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_annotation_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_annotation_store)
        """

    def get_annotation_store_version(
        self, **kwargs: Unpack[GetAnnotationStoreVersionRequestTypeDef]
    ) -> GetAnnotationStoreVersionResponseTypeDef:
        """
        Retrieves the metadata for an annotation store version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_annotation_store_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_annotation_store_version)
        """

    def get_read_set(self, **kwargs: Unpack[GetReadSetRequestTypeDef]) -> GetReadSetResponseTypeDef:
        """
        Retrieves detailed information from parts of a read set and returns the read
        set in the same format that it was uploaded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_read_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_read_set)
        """

    def get_read_set_activation_job(
        self, **kwargs: Unpack[GetReadSetActivationJobRequestTypeDef]
    ) -> GetReadSetActivationJobResponseTypeDef:
        """
        Returns detailed information about the status of a read set activation job in
        JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_read_set_activation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_read_set_activation_job)
        """

    def get_read_set_export_job(
        self, **kwargs: Unpack[GetReadSetExportJobRequestTypeDef]
    ) -> GetReadSetExportJobResponseTypeDef:
        """
        Retrieves status information about a read set export job and returns the data
        in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_read_set_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_read_set_export_job)
        """

    def get_read_set_import_job(
        self, **kwargs: Unpack[GetReadSetImportJobRequestTypeDef]
    ) -> GetReadSetImportJobResponseTypeDef:
        """
        Gets detailed and status information about a read set import job and returns
        the data in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_read_set_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_read_set_import_job)
        """

    def get_read_set_metadata(
        self, **kwargs: Unpack[GetReadSetMetadataRequestTypeDef]
    ) -> GetReadSetMetadataResponseTypeDef:
        """
        Retrieves the metadata for a read set from a sequence store in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_read_set_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_read_set_metadata)
        """

    def get_reference(
        self, **kwargs: Unpack[GetReferenceRequestTypeDef]
    ) -> GetReferenceResponseTypeDef:
        """
        Downloads parts of data from a reference genome and returns the reference file
        in the same format that it was uploaded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_reference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_reference)
        """

    def get_reference_import_job(
        self, **kwargs: Unpack[GetReferenceImportJobRequestTypeDef]
    ) -> GetReferenceImportJobResponseTypeDef:
        """
        Monitors the status of a reference import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_reference_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_reference_import_job)
        """

    def get_reference_metadata(
        self, **kwargs: Unpack[GetReferenceMetadataRequestTypeDef]
    ) -> GetReferenceMetadataResponseTypeDef:
        """
        Retrieves metadata for a reference genome.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_reference_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_reference_metadata)
        """

    def get_reference_store(
        self, **kwargs: Unpack[GetReferenceStoreRequestTypeDef]
    ) -> GetReferenceStoreResponseTypeDef:
        """
        Gets information about a reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_reference_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_reference_store)
        """

    def get_run(self, **kwargs: Unpack[GetRunRequestTypeDef]) -> GetRunResponseTypeDef:
        """
        Gets detailed information about a specific run using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_run)
        """

    def get_run_cache(
        self, **kwargs: Unpack[GetRunCacheRequestTypeDef]
    ) -> GetRunCacheResponseTypeDef:
        """
        Retrieves detailed information about the specified run cache using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_run_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_run_cache)
        """

    def get_run_group(
        self, **kwargs: Unpack[GetRunGroupRequestTypeDef]
    ) -> GetRunGroupResponseTypeDef:
        """
        Gets information about a run group and returns its metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_run_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_run_group)
        """

    def get_run_task(self, **kwargs: Unpack[GetRunTaskRequestTypeDef]) -> GetRunTaskResponseTypeDef:
        """
        Gets detailed information about a run task using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_run_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_run_task)
        """

    def get_s3_access_policy(
        self, **kwargs: Unpack[GetS3AccessPolicyRequestTypeDef]
    ) -> GetS3AccessPolicyResponseTypeDef:
        """
        Retrieves details about an access policy on a given store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_s3_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_s3_access_policy)
        """

    def get_sequence_store(
        self, **kwargs: Unpack[GetSequenceStoreRequestTypeDef]
    ) -> GetSequenceStoreResponseTypeDef:
        """
        Retrieves metadata for a sequence store using its ID and returns it in JSON
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_sequence_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_sequence_store)
        """

    def get_share(self, **kwargs: Unpack[GetShareRequestTypeDef]) -> GetShareResponseTypeDef:
        """
        Retrieves the metadata for the specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_share)
        """

    def get_variant_import_job(
        self, **kwargs: Unpack[GetVariantImportRequestTypeDef]
    ) -> GetVariantImportResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_variant_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_variant_import_job)
        """

    def get_variant_store(
        self, **kwargs: Unpack[GetVariantStoreRequestTypeDef]
    ) -> GetVariantStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_variant_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_variant_store)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetWorkflowRequestTypeDef]
    ) -> GetWorkflowResponseTypeDef:
        """
        Gets all information about a workflow using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_workflow)
        """

    def get_workflow_version(
        self, **kwargs: Unpack[GetWorkflowVersionRequestTypeDef]
    ) -> GetWorkflowVersionResponseTypeDef:
        """
        Gets information about a workflow version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_workflow_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_workflow_version)
        """

    def list_annotation_import_jobs(
        self, **kwargs: Unpack[ListAnnotationImportJobsRequestTypeDef]
    ) -> ListAnnotationImportJobsResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_annotation_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_annotation_import_jobs)
        """

    def list_annotation_store_versions(
        self, **kwargs: Unpack[ListAnnotationStoreVersionsRequestTypeDef]
    ) -> ListAnnotationStoreVersionsResponseTypeDef:
        """
        Lists the versions of an annotation store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_annotation_store_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_annotation_store_versions)
        """

    def list_annotation_stores(
        self, **kwargs: Unpack[ListAnnotationStoresRequestTypeDef]
    ) -> ListAnnotationStoresResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_annotation_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_annotation_stores)
        """

    def list_multipart_read_set_uploads(
        self, **kwargs: Unpack[ListMultipartReadSetUploadsRequestTypeDef]
    ) -> ListMultipartReadSetUploadsResponseTypeDef:
        """
        Lists in-progress multipart read set uploads for a sequence store and returns
        it in a JSON formatted output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_multipart_read_set_uploads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_multipart_read_set_uploads)
        """

    def list_read_set_activation_jobs(
        self, **kwargs: Unpack[ListReadSetActivationJobsRequestTypeDef]
    ) -> ListReadSetActivationJobsResponseTypeDef:
        """
        Retrieves a list of read set activation jobs and returns the metadata in a JSON
        formatted output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_read_set_activation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_read_set_activation_jobs)
        """

    def list_read_set_export_jobs(
        self, **kwargs: Unpack[ListReadSetExportJobsRequestTypeDef]
    ) -> ListReadSetExportJobsResponseTypeDef:
        """
        Retrieves a list of read set export jobs in a JSON formatted response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_read_set_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_read_set_export_jobs)
        """

    def list_read_set_import_jobs(
        self, **kwargs: Unpack[ListReadSetImportJobsRequestTypeDef]
    ) -> ListReadSetImportJobsResponseTypeDef:
        """
        Retrieves a list of read set import jobs and returns the data in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_read_set_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_read_set_import_jobs)
        """

    def list_read_set_upload_parts(
        self, **kwargs: Unpack[ListReadSetUploadPartsRequestTypeDef]
    ) -> ListReadSetUploadPartsResponseTypeDef:
        """
        Lists all parts in a multipart read set upload for a sequence store and returns
        the metadata in a JSON formatted output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_read_set_upload_parts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_read_set_upload_parts)
        """

    def list_read_sets(
        self, **kwargs: Unpack[ListReadSetsRequestTypeDef]
    ) -> ListReadSetsResponseTypeDef:
        """
        Retrieves a list of read sets from a sequence store ID and returns the metadata
        in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_read_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_read_sets)
        """

    def list_reference_import_jobs(
        self, **kwargs: Unpack[ListReferenceImportJobsRequestTypeDef]
    ) -> ListReferenceImportJobsResponseTypeDef:
        """
        Retrieves the metadata of one or more reference import jobs for a reference
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_reference_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_reference_import_jobs)
        """

    def list_reference_stores(
        self, **kwargs: Unpack[ListReferenceStoresRequestTypeDef]
    ) -> ListReferenceStoresResponseTypeDef:
        """
        Retrieves a list of reference stores linked to your account and returns their
        metadata in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_reference_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_reference_stores)
        """

    def list_references(
        self, **kwargs: Unpack[ListReferencesRequestTypeDef]
    ) -> ListReferencesResponseTypeDef:
        """
        Retrieves the metadata of one or more reference genomes in a reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_references.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_references)
        """

    def list_run_caches(
        self, **kwargs: Unpack[ListRunCachesRequestTypeDef]
    ) -> ListRunCachesResponseTypeDef:
        """
        Retrieves a list of your run caches and the metadata for each cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_run_caches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_run_caches)
        """

    def list_run_groups(
        self, **kwargs: Unpack[ListRunGroupsRequestTypeDef]
    ) -> ListRunGroupsResponseTypeDef:
        """
        Retrieves a list of all run groups and returns the metadata for each run group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_run_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_run_groups)
        """

    def list_run_tasks(
        self, **kwargs: Unpack[ListRunTasksRequestTypeDef]
    ) -> ListRunTasksResponseTypeDef:
        """
        Returns a list of tasks and status information within their specified run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_run_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_run_tasks)
        """

    def list_runs(self, **kwargs: Unpack[ListRunsRequestTypeDef]) -> ListRunsResponseTypeDef:
        """
        Retrieves a list of runs and returns each run's metadata and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_runs)
        """

    def list_sequence_stores(
        self, **kwargs: Unpack[ListSequenceStoresRequestTypeDef]
    ) -> ListSequenceStoresResponseTypeDef:
        """
        Retrieves a list of sequence stores and returns each sequence store's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_sequence_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_sequence_stores)
        """

    def list_shares(self, **kwargs: Unpack[ListSharesRequestTypeDef]) -> ListSharesResponseTypeDef:
        """
        Retrieves the resource shares associated with an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_shares)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_tags_for_resource)
        """

    def list_variant_import_jobs(
        self, **kwargs: Unpack[ListVariantImportJobsRequestTypeDef]
    ) -> ListVariantImportJobsResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_variant_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_variant_import_jobs)
        """

    def list_variant_stores(
        self, **kwargs: Unpack[ListVariantStoresRequestTypeDef]
    ) -> ListVariantStoresResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_variant_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_variant_stores)
        """

    def list_workflow_versions(
        self, **kwargs: Unpack[ListWorkflowVersionsRequestTypeDef]
    ) -> ListWorkflowVersionsResponseTypeDef:
        """
        Lists the workflow versions for the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_workflow_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_workflow_versions)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Retrieves a list of existing workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#list_workflows)
        """

    def put_s3_access_policy(
        self, **kwargs: Unpack[PutS3AccessPolicyRequestTypeDef]
    ) -> PutS3AccessPolicyResponseTypeDef:
        """
        Adds an access policy to the specified store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/put_s3_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#put_s3_access_policy)
        """

    def start_annotation_import_job(
        self, **kwargs: Unpack[StartAnnotationImportRequestTypeDef]
    ) -> StartAnnotationImportResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_annotation_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_annotation_import_job)
        """

    def start_read_set_activation_job(
        self, **kwargs: Unpack[StartReadSetActivationJobRequestTypeDef]
    ) -> StartReadSetActivationJobResponseTypeDef:
        """
        Activates an archived read set and returns its metadata in a JSON formatted
        output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_read_set_activation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_read_set_activation_job)
        """

    def start_read_set_export_job(
        self, **kwargs: Unpack[StartReadSetExportJobRequestTypeDef]
    ) -> StartReadSetExportJobResponseTypeDef:
        """
        Starts a read set export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_read_set_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_read_set_export_job)
        """

    def start_read_set_import_job(
        self, **kwargs: Unpack[StartReadSetImportJobRequestTypeDef]
    ) -> StartReadSetImportJobResponseTypeDef:
        """
        Imports a read set from the sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_read_set_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_read_set_import_job)
        """

    def start_reference_import_job(
        self, **kwargs: Unpack[StartReferenceImportJobRequestTypeDef]
    ) -> StartReferenceImportJobResponseTypeDef:
        """
        Imports a reference genome from Amazon S3 into a specified reference store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_reference_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_reference_import_job)
        """

    def start_run(self, **kwargs: Unpack[StartRunRequestTypeDef]) -> StartRunResponseTypeDef:
        """
        Starts a new run and returns details about the run, or duplicates an existing
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_run)
        """

    def start_variant_import_job(
        self, **kwargs: Unpack[StartVariantImportRequestTypeDef]
    ) -> StartVariantImportResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/start_variant_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#start_variant_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#untag_resource)
        """

    def update_annotation_store(
        self, **kwargs: Unpack[UpdateAnnotationStoreRequestTypeDef]
    ) -> UpdateAnnotationStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_annotation_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_annotation_store)
        """

    def update_annotation_store_version(
        self, **kwargs: Unpack[UpdateAnnotationStoreVersionRequestTypeDef]
    ) -> UpdateAnnotationStoreVersionResponseTypeDef:
        """
        Updates the description of an annotation store version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_annotation_store_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_annotation_store_version)
        """

    def update_run_cache(
        self, **kwargs: Unpack[UpdateRunCacheRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a run cache using its ID and returns a response with no body if the
        operation is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_run_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_run_cache)
        """

    def update_run_group(
        self, **kwargs: Unpack[UpdateRunGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the settings of a run group and returns a response with no body if the
        operation is successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_run_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_run_group)
        """

    def update_sequence_store(
        self, **kwargs: Unpack[UpdateSequenceStoreRequestTypeDef]
    ) -> UpdateSequenceStoreResponseTypeDef:
        """
        Update one or more parameters for the sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_sequence_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_sequence_store)
        """

    def update_variant_store(
        self, **kwargs: Unpack[UpdateVariantStoreRequestTypeDef]
    ) -> UpdateVariantStoreResponseTypeDef:
        """
        <important> <p>Amazon Web Services HealthOmics variant stores and annotation
        stores will no longer be open to new customers starting November 7, 2025.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_variant_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_variant_store)
        """

    def update_workflow(
        self, **kwargs: Unpack[UpdateWorkflowRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates information about a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_workflow)
        """

    def update_workflow_version(
        self, **kwargs: Unpack[UpdateWorkflowVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates information about the workflow version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/update_workflow_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#update_workflow_version)
        """

    def upload_read_set_part(
        self, **kwargs: Unpack[UploadReadSetPartRequestTypeDef]
    ) -> UploadReadSetPartResponseTypeDef:
        """
        Uploads a specific part of a read set into a sequence store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/upload_read_set_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#upload_read_set_part)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_annotation_import_jobs"]
    ) -> ListAnnotationImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_annotation_store_versions"]
    ) -> ListAnnotationStoreVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_annotation_stores"]
    ) -> ListAnnotationStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_multipart_read_set_uploads"]
    ) -> ListMultipartReadSetUploadsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_read_set_activation_jobs"]
    ) -> ListReadSetActivationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_read_set_export_jobs"]
    ) -> ListReadSetExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_read_set_import_jobs"]
    ) -> ListReadSetImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_read_set_upload_parts"]
    ) -> ListReadSetUploadPartsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_read_sets"]
    ) -> ListReadSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reference_import_jobs"]
    ) -> ListReferenceImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reference_stores"]
    ) -> ListReferenceStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_references"]
    ) -> ListReferencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_run_caches"]
    ) -> ListRunCachesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_run_groups"]
    ) -> ListRunGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_run_tasks"]
    ) -> ListRunTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_runs"]
    ) -> ListRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sequence_stores"]
    ) -> ListSequenceStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_shares"]
    ) -> ListSharesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_variant_import_jobs"]
    ) -> ListVariantImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_variant_stores"]
    ) -> ListVariantStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_versions"]
    ) -> ListWorkflowVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflows"]
    ) -> ListWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["annotation_import_job_created"]
    ) -> AnnotationImportJobCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["annotation_store_created"]
    ) -> AnnotationStoreCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["annotation_store_deleted"]
    ) -> AnnotationStoreDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["annotation_store_version_created"]
    ) -> AnnotationStoreVersionCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["annotation_store_version_deleted"]
    ) -> AnnotationStoreVersionDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["read_set_activation_job_completed"]
    ) -> ReadSetActivationJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["read_set_export_job_completed"]
    ) -> ReadSetExportJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["read_set_import_job_completed"]
    ) -> ReadSetImportJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["reference_import_job_completed"]
    ) -> ReferenceImportJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["run_completed"]
    ) -> RunCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["run_running"]
    ) -> RunRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["task_completed"]
    ) -> TaskCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["task_running"]
    ) -> TaskRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["variant_import_job_created"]
    ) -> VariantImportJobCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["variant_store_created"]
    ) -> VariantStoreCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["variant_store_deleted"]
    ) -> VariantStoreDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["workflow_active"]
    ) -> WorkflowActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["workflow_version_active"]
    ) -> WorkflowVersionActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/client/#get_waiter)
        """
