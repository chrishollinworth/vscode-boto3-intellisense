"""
Type annotations for importexport service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_importexport import ImportExportClient

    client: ImportExportClient = boto3.client("importexport")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import JobTypeType
from .paginator import ListJobsPaginator
from .type_defs import (
    CancelJobOutputTypeDef,
    CreateJobOutputTypeDef,
    GetShippingLabelOutputTypeDef,
    GetStatusOutputTypeDef,
    ListJobsOutputTypeDef,
    UpdateJobOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ImportExportClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BucketPermissionException: Type[BotocoreClientError]
    CanceledJobIdException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreateJobQuotaExceededException: Type[BotocoreClientError]
    ExpiredJobIdException: Type[BotocoreClientError]
    InvalidAccessKeyIdException: Type[BotocoreClientError]
    InvalidAddressException: Type[BotocoreClientError]
    InvalidCustomsException: Type[BotocoreClientError]
    InvalidFileSystemException: Type[BotocoreClientError]
    InvalidJobIdException: Type[BotocoreClientError]
    InvalidManifestFieldException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidVersionException: Type[BotocoreClientError]
    MalformedManifestException: Type[BotocoreClientError]
    MissingCustomsException: Type[BotocoreClientError]
    MissingManifestFieldException: Type[BotocoreClientError]
    MissingParameterException: Type[BotocoreClientError]
    MultipleRegionsException: Type[BotocoreClientError]
    NoSuchBucketException: Type[BotocoreClientError]
    UnableToCancelJobIdException: Type[BotocoreClientError]
    UnableToUpdateJobIdException: Type[BotocoreClientError]

class ImportExportClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ImportExportClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#can_paginate)
        """
    def cancel_job(self, *, JobId: str, APIVersion: str = None) -> CancelJobOutputTypeDef:
        """
        This operation cancels a specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#cancel_job)
        """
    def create_job(
        self,
        *,
        JobType: JobTypeType,
        Manifest: str,
        ValidateOnly: bool,
        ManifestAddendum: str = None,
        APIVersion: str = None
    ) -> CreateJobOutputTypeDef:
        """
        This operation initiates the process of scheduling an upload or download of your
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#create_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#generate_presigned_url)
        """
    def get_shipping_label(
        self,
        *,
        jobIds: List[str],
        name: str = None,
        company: str = None,
        phoneNumber: str = None,
        country: str = None,
        stateOrProvince: str = None,
        city: str = None,
        postalCode: str = None,
        street1: str = None,
        street2: str = None,
        street3: str = None,
        APIVersion: str = None
    ) -> GetShippingLabelOutputTypeDef:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship
        your device to AWS for processing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.get_shipping_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#get_shipping_label)
        """
    def get_status(self, *, JobId: str, APIVersion: str = None) -> GetStatusOutputTypeDef:
        """
        This operation returns information about a job, including where the job is in
        the processing pipeline, the status of the results, and the signature value
        associated with the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.get_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#get_status)
        """
    def list_jobs(
        self, *, MaxJobs: int = None, Marker: str = None, APIVersion: str = None
    ) -> ListJobsOutputTypeDef:
        """
        This operation returns the jobs associated with the requester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#list_jobs)
        """
    def update_job(
        self,
        *,
        JobId: str,
        Manifest: str,
        JobType: JobTypeType,
        ValidateOnly: bool,
        APIVersion: str = None
    ) -> UpdateJobOutputTypeDef:
        """
        You use this operation to change the parameters specified in the original
        manifest file by supplying a new manifest file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/client.html#update_job)
        """
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/importexport.html#ImportExport.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/paginators.html#listjobspaginator)
        """
