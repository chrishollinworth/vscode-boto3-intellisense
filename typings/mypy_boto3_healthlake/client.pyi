"""
Type annotations for healthlake service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_healthlake.client import HealthLakeClient

    session = Session()
    client: HealthLakeClient = session.client("healthlake")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateFHIRDatastoreRequestTypeDef,
    CreateFHIRDatastoreResponseTypeDef,
    DeleteFHIRDatastoreRequestTypeDef,
    DeleteFHIRDatastoreResponseTypeDef,
    DescribeFHIRDatastoreRequestTypeDef,
    DescribeFHIRDatastoreResponseTypeDef,
    DescribeFHIRExportJobRequestTypeDef,
    DescribeFHIRExportJobResponseTypeDef,
    DescribeFHIRImportJobRequestTypeDef,
    DescribeFHIRImportJobResponseTypeDef,
    ListFHIRDatastoresRequestTypeDef,
    ListFHIRDatastoresResponseTypeDef,
    ListFHIRExportJobsRequestTypeDef,
    ListFHIRExportJobsResponseTypeDef,
    ListFHIRImportJobsRequestTypeDef,
    ListFHIRImportJobsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartFHIRExportJobRequestTypeDef,
    StartFHIRExportJobResponseTypeDef,
    StartFHIRImportJobRequestTypeDef,
    StartFHIRImportJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)
from .waiter import (
    FHIRDatastoreActiveWaiter,
    FHIRDatastoreDeletedWaiter,
    FHIRExportJobCompletedWaiter,
    FHIRImportJobCompletedWaiter,
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

__all__ = ("HealthLakeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class HealthLakeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HealthLakeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html#HealthLake.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#generate_presigned_url)
        """

    def create_fhir_datastore(
        self, **kwargs: Unpack[CreateFHIRDatastoreRequestTypeDef]
    ) -> CreateFHIRDatastoreResponseTypeDef:
        """
        Create a FHIR-enabled data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/create_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#create_fhir_datastore)
        """

    def delete_fhir_datastore(
        self, **kwargs: Unpack[DeleteFHIRDatastoreRequestTypeDef]
    ) -> DeleteFHIRDatastoreResponseTypeDef:
        """
        Delete a FHIR-enabled data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/delete_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#delete_fhir_datastore)
        """

    def describe_fhir_datastore(
        self, **kwargs: Unpack[DescribeFHIRDatastoreRequestTypeDef]
    ) -> DescribeFHIRDatastoreResponseTypeDef:
        """
        Get properties for a FHIR-enabled data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_datastore)
        """

    def describe_fhir_export_job(
        self, **kwargs: Unpack[DescribeFHIRExportJobRequestTypeDef]
    ) -> DescribeFHIRExportJobResponseTypeDef:
        """
        Get FHIR export job properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_export_job)
        """

    def describe_fhir_import_job(
        self, **kwargs: Unpack[DescribeFHIRImportJobRequestTypeDef]
    ) -> DescribeFHIRImportJobResponseTypeDef:
        """
        Get the import job properties to learn more about the job or job progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_import_job)
        """

    def list_fhir_datastores(
        self, **kwargs: Unpack[ListFHIRDatastoresRequestTypeDef]
    ) -> ListFHIRDatastoresResponseTypeDef:
        """
        List all FHIR-enabled data stores in a user's account, regardless of data store
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/list_fhir_datastores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#list_fhir_datastores)
        """

    def list_fhir_export_jobs(
        self, **kwargs: Unpack[ListFHIRExportJobsRequestTypeDef]
    ) -> ListFHIRExportJobsResponseTypeDef:
        """
        Lists all FHIR export jobs associated with an account and their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/list_fhir_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#list_fhir_export_jobs)
        """

    def list_fhir_import_jobs(
        self, **kwargs: Unpack[ListFHIRImportJobsRequestTypeDef]
    ) -> ListFHIRImportJobsResponseTypeDef:
        """
        List all FHIR import jobs associated with an account and their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/list_fhir_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#list_fhir_import_jobs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all existing tags associated with a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#list_tags_for_resource)
        """

    def start_fhir_export_job(
        self, **kwargs: Unpack[StartFHIRExportJobRequestTypeDef]
    ) -> StartFHIRExportJobResponseTypeDef:
        """
        Start a FHIR export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/start_fhir_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#start_fhir_export_job)
        """

    def start_fhir_import_job(
        self, **kwargs: Unpack[StartFHIRImportJobRequestTypeDef]
    ) -> StartFHIRImportJobResponseTypeDef:
        """
        Start importing bulk FHIR data into an ACTIVE data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/start_fhir_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#start_fhir_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add a user-specifed key and value tag to a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove a user-specifed key and value tag from a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fhir_datastore_active"]
    ) -> FHIRDatastoreActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fhir_datastore_deleted"]
    ) -> FHIRDatastoreDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fhir_export_job_completed"]
    ) -> FHIRExportJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fhir_import_job_completed"]
    ) -> FHIRImportJobCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#get_waiter)
        """
