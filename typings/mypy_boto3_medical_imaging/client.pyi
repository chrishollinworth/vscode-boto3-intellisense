"""
Type annotations for medical-imaging service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_medical_imaging.client import HealthImagingClient

    session = Session()
    client: HealthImagingClient = session.client("medical-imaging")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDatastoresPaginator,
    ListDICOMImportJobsPaginator,
    ListImageSetVersionsPaginator,
    SearchImageSetsPaginator,
)
from .type_defs import (
    CopyImageSetRequestTypeDef,
    CopyImageSetResponseTypeDef,
    CreateDatastoreRequestTypeDef,
    CreateDatastoreResponseTypeDef,
    DeleteDatastoreRequestTypeDef,
    DeleteDatastoreResponseTypeDef,
    DeleteImageSetRequestTypeDef,
    DeleteImageSetResponseTypeDef,
    GetDatastoreRequestTypeDef,
    GetDatastoreResponseTypeDef,
    GetDICOMImportJobRequestTypeDef,
    GetDICOMImportJobResponseTypeDef,
    GetImageFrameRequestTypeDef,
    GetImageFrameResponseTypeDef,
    GetImageSetMetadataRequestTypeDef,
    GetImageSetMetadataResponseTypeDef,
    GetImageSetRequestTypeDef,
    GetImageSetResponseTypeDef,
    ListDatastoresRequestTypeDef,
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsRequestTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsRequestTypeDef,
    ListImageSetVersionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchImageSetsRequestTypeDef,
    SearchImageSetsResponseTypeDef,
    StartDICOMImportJobRequestTypeDef,
    StartDICOMImportJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateImageSetMetadataRequestTypeDef,
    UpdateImageSetMetadataResponseTypeDef,
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

__all__ = ("HealthImagingClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class HealthImagingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HealthImagingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#generate_presigned_url)
        """

    def copy_image_set(
        self, **kwargs: Unpack[CopyImageSetRequestTypeDef]
    ) -> CopyImageSetResponseTypeDef:
        """
        Copy an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/copy_image_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#copy_image_set)
        """

    def create_datastore(
        self, **kwargs: Unpack[CreateDatastoreRequestTypeDef]
    ) -> CreateDatastoreResponseTypeDef:
        """
        Create a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/create_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#create_datastore)
        """

    def delete_datastore(
        self, **kwargs: Unpack[DeleteDatastoreRequestTypeDef]
    ) -> DeleteDatastoreResponseTypeDef:
        """
        Delete a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/delete_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#delete_datastore)
        """

    def delete_image_set(
        self, **kwargs: Unpack[DeleteImageSetRequestTypeDef]
    ) -> DeleteImageSetResponseTypeDef:
        """
        Delete an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/delete_image_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#delete_image_set)
        """

    def get_dicom_import_job(
        self, **kwargs: Unpack[GetDICOMImportJobRequestTypeDef]
    ) -> GetDICOMImportJobResponseTypeDef:
        """
        Get the import job properties to learn more about the job or job progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_dicom_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_dicom_import_job)
        """

    def get_datastore(
        self, **kwargs: Unpack[GetDatastoreRequestTypeDef]
    ) -> GetDatastoreResponseTypeDef:
        """
        Get data store properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_datastore)
        """

    def get_image_frame(
        self, **kwargs: Unpack[GetImageFrameRequestTypeDef]
    ) -> GetImageFrameResponseTypeDef:
        """
        Get an image frame (pixel data) for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_image_frame.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_image_frame)
        """

    def get_image_set(
        self, **kwargs: Unpack[GetImageSetRequestTypeDef]
    ) -> GetImageSetResponseTypeDef:
        """
        Get image set properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_image_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_image_set)
        """

    def get_image_set_metadata(
        self, **kwargs: Unpack[GetImageSetMetadataRequestTypeDef]
    ) -> GetImageSetMetadataResponseTypeDef:
        """
        Get metadata attributes for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_image_set_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_image_set_metadata)
        """

    def list_dicom_import_jobs(
        self, **kwargs: Unpack[ListDICOMImportJobsRequestTypeDef]
    ) -> ListDICOMImportJobsResponseTypeDef:
        """
        List import jobs created for a specific data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/list_dicom_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#list_dicom_import_jobs)
        """

    def list_datastores(
        self, **kwargs: Unpack[ListDatastoresRequestTypeDef]
    ) -> ListDatastoresResponseTypeDef:
        """
        List data stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/list_datastores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#list_datastores)
        """

    def list_image_set_versions(
        self, **kwargs: Unpack[ListImageSetVersionsRequestTypeDef]
    ) -> ListImageSetVersionsResponseTypeDef:
        """
        List image set versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/list_image_set_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#list_image_set_versions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#list_tags_for_resource)
        """

    def search_image_sets(
        self, **kwargs: Unpack[SearchImageSetsRequestTypeDef]
    ) -> SearchImageSetsResponseTypeDef:
        """
        Search image sets based on defined input attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/search_image_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#search_image_sets)
        """

    def start_dicom_import_job(
        self, **kwargs: Unpack[StartDICOMImportJobRequestTypeDef]
    ) -> StartDICOMImportJobResponseTypeDef:
        """
        Start importing bulk data into an <code>ACTIVE</code> data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/start_dicom_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#start_dicom_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a user-specifed key and value tag to a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#untag_resource)
        """

    def update_image_set_metadata(
        self, **kwargs: Unpack[UpdateImageSetMetadataRequestTypeDef]
    ) -> UpdateImageSetMetadataResponseTypeDef:
        """
        Update image set metadata attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/update_image_set_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#update_image_set_metadata)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dicom_import_jobs"]
    ) -> ListDICOMImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datastores"]
    ) -> ListDatastoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_image_set_versions"]
    ) -> ListImageSetVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_image_sets"]
    ) -> SearchImageSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client/#get_paginator)
        """
