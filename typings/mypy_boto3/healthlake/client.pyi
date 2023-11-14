"""
Type annotations for healthlake service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_healthlake import HealthLakeClient

    client: HealthLakeClient = boto3.client("healthlake")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import JobStatusType
from .type_defs import (
    CreateFHIRDatastoreResponseTypeDef,
    DatastoreFilterTypeDef,
    DeleteFHIRDatastoreResponseTypeDef,
    DescribeFHIRDatastoreResponseTypeDef,
    DescribeFHIRExportJobResponseTypeDef,
    DescribeFHIRImportJobResponseTypeDef,
    IdentityProviderConfigurationTypeDef,
    InputDataConfigTypeDef,
    ListFHIRDatastoresResponseTypeDef,
    ListFHIRExportJobsResponseTypeDef,
    ListFHIRImportJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputDataConfigTypeDef,
    PreloadDataConfigTypeDef,
    SseConfigurationTypeDef,
    StartFHIRExportJobResponseTypeDef,
    StartFHIRImportJobResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("HealthLakeClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class HealthLakeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HealthLakeClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#close)
        """
    def create_fhir_datastore(
        self,
        *,
        DatastoreTypeVersion: Literal["R4"],
        DatastoreName: str = None,
        SseConfiguration: "SseConfigurationTypeDef" = None,
        PreloadDataConfig: "PreloadDataConfigTypeDef" = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
        IdentityProviderConfiguration: "IdentityProviderConfigurationTypeDef" = None
    ) -> CreateFHIRDatastoreResponseTypeDef:
        """
        Creates a data store that can ingest and export FHIR formatted data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.create_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#create_fhir_datastore)
        """
    def delete_fhir_datastore(self, *, DatastoreId: str) -> DeleteFHIRDatastoreResponseTypeDef:
        """
        Deletes a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.delete_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#delete_fhir_datastore)
        """
    def describe_fhir_datastore(self, *, DatastoreId: str) -> DescribeFHIRDatastoreResponseTypeDef:
        """
        Gets the properties associated with the FHIR data store, including the data
        store ID, data store ARN, data store name, data store status, when the data
        store was created, data store type version, and the data store's endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.describe_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_datastore)
        """
    def describe_fhir_export_job(
        self, *, DatastoreId: str, JobId: str
    ) -> DescribeFHIRExportJobResponseTypeDef:
        """
        Displays the properties of a FHIR export job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.describe_fhir_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_export_job)
        """
    def describe_fhir_import_job(
        self, *, DatastoreId: str, JobId: str
    ) -> DescribeFHIRImportJobResponseTypeDef:
        """
        Displays the properties of a FHIR import job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.describe_fhir_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_import_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#generate_presigned_url)
        """
    def list_fhir_datastores(
        self,
        *,
        Filter: "DatastoreFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFHIRDatastoresResponseTypeDef:
        """
        Lists all FHIR data stores that are in the user’s account, regardless of data
        store status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.list_fhir_datastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#list_fhir_datastores)
        """
    def list_fhir_export_jobs(
        self,
        *,
        DatastoreId: str,
        NextToken: str = None,
        MaxResults: int = None,
        JobName: str = None,
        JobStatus: JobStatusType = None,
        SubmittedBefore: Union[datetime, str] = None,
        SubmittedAfter: Union[datetime, str] = None
    ) -> ListFHIRExportJobsResponseTypeDef:
        """
        Lists all FHIR export jobs associated with an account and their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.list_fhir_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#list_fhir_export_jobs)
        """
    def list_fhir_import_jobs(
        self,
        *,
        DatastoreId: str,
        NextToken: str = None,
        MaxResults: int = None,
        JobName: str = None,
        JobStatus: JobStatusType = None,
        SubmittedBefore: Union[datetime, str] = None,
        SubmittedAfter: Union[datetime, str] = None
    ) -> ListFHIRImportJobsResponseTypeDef:
        """
        Lists all FHIR import jobs associated with an account and their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.list_fhir_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#list_fhir_import_jobs)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all existing tags associated with a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#list_tags_for_resource)
        """
    def start_fhir_export_job(
        self,
        *,
        OutputDataConfig: "OutputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None
    ) -> StartFHIRExportJobResponseTypeDef:
        """
        Begins a FHIR export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.start_fhir_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#start_fhir_export_job)
        """
    def start_fhir_import_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        JobOutputDataConfig: "OutputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None
    ) -> StartFHIRImportJobResponseTypeDef:
        """
        Begins a FHIR Import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.start_fhir_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#start_fhir_import_job)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds a user specified key and value tag to a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/healthlake.html#HealthLake.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#untag_resource)
        """
