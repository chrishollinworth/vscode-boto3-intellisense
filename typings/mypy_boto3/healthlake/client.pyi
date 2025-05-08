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
from typing import Any

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
        Creates a data store that can ingest and export FHIR formatted data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/create_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#create_fhir_datastore)
        """

    def delete_fhir_datastore(
        self, **kwargs: Unpack[DeleteFHIRDatastoreRequestTypeDef]
    ) -> DeleteFHIRDatastoreResponseTypeDef:
        """
        Deletes a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/delete_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#delete_fhir_datastore)
        """

    def describe_fhir_datastore(
        self, **kwargs: Unpack[DescribeFHIRDatastoreRequestTypeDef]
    ) -> DescribeFHIRDatastoreResponseTypeDef:
        """
        Gets the properties associated with the FHIR data store, including the data
        store ID, data store ARN, data store name, data store status, when the data
        store was created, data store type version, and the data store's endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_datastore)
        """

    def describe_fhir_export_job(
        self, **kwargs: Unpack[DescribeFHIRExportJobRequestTypeDef]
    ) -> DescribeFHIRExportJobResponseTypeDef:
        """
        Displays the properties of a FHIR export job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_export_job)
        """

    def describe_fhir_import_job(
        self, **kwargs: Unpack[DescribeFHIRImportJobRequestTypeDef]
    ) -> DescribeFHIRImportJobResponseTypeDef:
        """
        Displays the properties of a FHIR import job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/describe_fhir_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#describe_fhir_import_job)
        """

    def list_fhir_datastores(
        self, **kwargs: Unpack[ListFHIRDatastoresRequestTypeDef]
    ) -> ListFHIRDatastoresResponseTypeDef:
        """
        Lists all FHIR data stores that are in the user's account, regardless of data
        store status.

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
        Lists all FHIR import jobs associated with an account and their statuses.

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
        Begins a FHIR export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/start_fhir_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#start_fhir_export_job)
        """

    def start_fhir_import_job(
        self, **kwargs: Unpack[StartFHIRImportJobRequestTypeDef]
    ) -> StartFHIRImportJobResponseTypeDef:
        """
        Begins a FHIR Import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/start_fhir_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#start_fhir_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a user specified key and value tag to a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client/#untag_resource)
        """
