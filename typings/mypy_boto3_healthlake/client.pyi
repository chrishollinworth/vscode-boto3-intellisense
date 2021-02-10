"""
Main interface for healthlake service client

Usage::

    ```python
    import boto3
    from mypy_boto3_healthlake import HealthLakeClient

    client: HealthLakeClient = boto3.client("healthlake")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_healthlake.type_defs import (
    CreateFHIRDatastoreResponseTypeDef,
    DatastoreFilterTypeDef,
    DeleteFHIRDatastoreResponseTypeDef,
    DescribeFHIRDatastoreResponseTypeDef,
    DescribeFHIRExportJobResponseTypeDef,
    DescribeFHIRImportJobResponseTypeDef,
    InputDataConfigTypeDef,
    ListFHIRDatastoresResponseTypeDef,
    OutputDataConfigTypeDef,
    PreloadDataConfigTypeDef,
    StartFHIRExportJobResponseTypeDef,
    StartFHIRImportJobResponseTypeDef,
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


class HealthLakeClient:
    """
    [HealthLake.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.can_paginate)
        """

    def create_fhir_datastore(
        self,
        DatastoreTypeVersion: Literal["R4"],
        DatastoreName: str = None,
        PreloadDataConfig: "PreloadDataConfigTypeDef" = None,
        ClientToken: str = None,
    ) -> CreateFHIRDatastoreResponseTypeDef:
        """
        [Client.create_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.create_fhir_datastore)
        """

    def delete_fhir_datastore(self, DatastoreId: str = None) -> DeleteFHIRDatastoreResponseTypeDef:
        """
        [Client.delete_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.delete_fhir_datastore)
        """

    def describe_fhir_datastore(
        self, DatastoreId: str = None
    ) -> DescribeFHIRDatastoreResponseTypeDef:
        """
        [Client.describe_fhir_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.describe_fhir_datastore)
        """

    def describe_fhir_export_job(
        self, DatastoreId: str, JobId: str
    ) -> DescribeFHIRExportJobResponseTypeDef:
        """
        [Client.describe_fhir_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.describe_fhir_export_job)
        """

    def describe_fhir_import_job(
        self, DatastoreId: str, JobId: str
    ) -> DescribeFHIRImportJobResponseTypeDef:
        """
        [Client.describe_fhir_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.describe_fhir_import_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.generate_presigned_url)
        """

    def list_fhir_datastores(
        self, Filter: DatastoreFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListFHIRDatastoresResponseTypeDef:
        """
        [Client.list_fhir_datastores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.list_fhir_datastores)
        """

    def start_fhir_export_job(
        self,
        OutputDataConfig: "OutputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None,
    ) -> StartFHIRExportJobResponseTypeDef:
        """
        [Client.start_fhir_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.start_fhir_export_job)
        """

    def start_fhir_import_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None,
    ) -> StartFHIRImportJobResponseTypeDef:
        """
        [Client.start_fhir_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/healthlake.html#HealthLake.Client.start_fhir_import_job)
        """
