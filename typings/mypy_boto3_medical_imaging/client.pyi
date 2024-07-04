"""
Type annotations for medical-imaging service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_medical_imaging import HealthImagingClient

    client: HealthImagingClient = boto3.client("medical-imaging")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import DatastoreStatusType, JobStatusType
from .paginator import (
    ListDatastoresPaginator,
    ListDICOMImportJobsPaginator,
    ListImageSetVersionsPaginator,
    SearchImageSetsPaginator,
)
from .type_defs import (
    CopyImageSetInformationTypeDef,
    CopyImageSetResponseTypeDef,
    CreateDatastoreResponseTypeDef,
    DeleteDatastoreResponseTypeDef,
    DeleteImageSetResponseTypeDef,
    GetDatastoreResponseTypeDef,
    GetDICOMImportJobResponseTypeDef,
    GetImageFrameResponseTypeDef,
    GetImageSetMetadataResponseTypeDef,
    GetImageSetResponseTypeDef,
    ImageFrameInformationTypeDef,
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetadataUpdatesTypeDef,
    SearchCriteriaTypeDef,
    SearchImageSetsResponseTypeDef,
    StartDICOMImportJobResponseTypeDef,
    UpdateImageSetMetadataResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("HealthImagingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HealthImagingClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#close)
        """

    def copy_image_set(
        self,
        *,
        datastoreId: str,
        sourceImageSetId: str,
        copyImageSetInformation: "CopyImageSetInformationTypeDef"
    ) -> CopyImageSetResponseTypeDef:
        """
        Copy an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.copy_image_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#copy_image_set)
        """

    def create_datastore(
        self,
        *,
        clientToken: str,
        datastoreName: str = None,
        tags: Dict[str, str] = None,
        kmsKeyArn: str = None
    ) -> CreateDatastoreResponseTypeDef:
        """
        Create a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.create_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#create_datastore)
        """

    def delete_datastore(self, *, datastoreId: str) -> DeleteDatastoreResponseTypeDef:
        """
        Delete a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.delete_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#delete_datastore)
        """

    def delete_image_set(
        self, *, datastoreId: str, imageSetId: str
    ) -> DeleteImageSetResponseTypeDef:
        """
        Delete an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.delete_image_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#delete_image_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#generate_presigned_url)
        """

    def get_datastore(self, *, datastoreId: str) -> GetDatastoreResponseTypeDef:
        """
        Get data store properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.get_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#get_datastore)
        """

    def get_dicom_import_job(
        self, *, datastoreId: str, jobId: str
    ) -> GetDICOMImportJobResponseTypeDef:
        """
        Get the import job properties to learn more about the job or job progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.get_dicom_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#get_dicom_import_job)
        """

    def get_image_frame(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        imageFrameInformation: "ImageFrameInformationTypeDef"
    ) -> GetImageFrameResponseTypeDef:
        """
        Get an image frame (pixel data) for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.get_image_frame)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#get_image_frame)
        """

    def get_image_set(
        self, *, datastoreId: str, imageSetId: str, versionId: str = None
    ) -> GetImageSetResponseTypeDef:
        """
        Get image set properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.get_image_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#get_image_set)
        """

    def get_image_set_metadata(
        self, *, datastoreId: str, imageSetId: str, versionId: str = None
    ) -> GetImageSetMetadataResponseTypeDef:
        """
        Get metadata attributes for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.get_image_set_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#get_image_set_metadata)
        """

    def list_datastores(
        self,
        *,
        datastoreStatus: DatastoreStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListDatastoresResponseTypeDef:
        """
        List data stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.list_datastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#list_datastores)
        """

    def list_dicom_import_jobs(
        self,
        *,
        datastoreId: str,
        jobStatus: JobStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListDICOMImportJobsResponseTypeDef:
        """
        List import jobs created for a specific data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.list_dicom_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#list_dicom_import_jobs)
        """

    def list_image_set_versions(
        self, *, datastoreId: str, imageSetId: str, nextToken: str = None, maxResults: int = None
    ) -> ListImageSetVersionsResponseTypeDef:
        """
        List image set versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.list_image_set_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#list_image_set_versions)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#list_tags_for_resource)
        """

    def search_image_sets(
        self,
        *,
        datastoreId: str,
        searchCriteria: "SearchCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchImageSetsResponseTypeDef:
        """
        Search image sets based on defined input attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.search_image_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#search_image_sets)
        """

    def start_dicom_import_job(
        self,
        *,
        dataAccessRoleArn: str,
        clientToken: str,
        datastoreId: str,
        inputS3Uri: str,
        outputS3Uri: str,
        jobName: str = None,
        inputOwnerAccountId: str = None
    ) -> StartDICOMImportJobResponseTypeDef:
        """
        Start importing bulk data into an `ACTIVE` data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.start_dicom_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#start_dicom_import_job)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds a user-specifed key and value tag to a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#untag_resource)
        """

    def update_image_set_metadata(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        latestVersionId: str,
        updateImageSetMetadataUpdates: "MetadataUpdatesTypeDef"
    ) -> UpdateImageSetMetadataResponseTypeDef:
        """
        Update image set metadata attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Client.update_image_set_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/client.html#update_image_set_metadata)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dicom_import_jobs"]
    ) -> ListDICOMImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDICOMImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdicomimportjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datastores"]) -> ListDatastoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDatastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listdatastorespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_set_versions"]
    ) -> ListImageSetVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Paginator.ListImageSetVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#listimagesetversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_image_sets"]
    ) -> SearchImageSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/medical-imaging.html#HealthImaging.Paginator.SearchImageSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/paginators.html#searchimagesetspaginator)
        """
