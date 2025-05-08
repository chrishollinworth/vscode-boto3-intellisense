"""
Type annotations for timestream-write service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_timestream_write.client import TimestreamWriteClient

    session = Session()
    client: TimestreamWriteClient = session.client("timestream-write")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateBatchLoadTaskRequestTypeDef,
    CreateBatchLoadTaskResponseTypeDef,
    CreateDatabaseRequestTypeDef,
    CreateDatabaseResponseTypeDef,
    CreateTableRequestTypeDef,
    CreateTableResponseTypeDef,
    DeleteDatabaseRequestTypeDef,
    DeleteTableRequestTypeDef,
    DescribeBatchLoadTaskRequestTypeDef,
    DescribeBatchLoadTaskResponseTypeDef,
    DescribeDatabaseRequestTypeDef,
    DescribeDatabaseResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeTableRequestTypeDef,
    DescribeTableResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListBatchLoadTasksRequestTypeDef,
    ListBatchLoadTasksResponseTypeDef,
    ListDatabasesRequestTypeDef,
    ListDatabasesResponseTypeDef,
    ListTablesRequestTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResumeBatchLoadTaskRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDatabaseRequestTypeDef,
    UpdateDatabaseResponseTypeDef,
    UpdateTableRequestTypeDef,
    UpdateTableResponseTypeDef,
    WriteRecordsRequestTypeDef,
    WriteRecordsResponseTypeDef,
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

__all__ = ("TimestreamWriteClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidEndpointException: Type[BotocoreClientError]
    RejectedRecordsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TimestreamWriteClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TimestreamWriteClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#generate_presigned_url)
        """

    def create_batch_load_task(
        self, **kwargs: Unpack[CreateBatchLoadTaskRequestTypeDef]
    ) -> CreateBatchLoadTaskResponseTypeDef:
        """
        Creates a new Timestream batch load task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/create_batch_load_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#create_batch_load_task)
        """

    def create_database(
        self, **kwargs: Unpack[CreateDatabaseRequestTypeDef]
    ) -> CreateDatabaseResponseTypeDef:
        """
        Creates a new Timestream database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/create_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#create_database)
        """

    def create_table(
        self, **kwargs: Unpack[CreateTableRequestTypeDef]
    ) -> CreateTableResponseTypeDef:
        """
        Adds a new table to an existing database in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/create_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#create_table)
        """

    def delete_database(
        self, **kwargs: Unpack[DeleteDatabaseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a given Timestream database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/delete_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#delete_database)
        """

    def delete_table(
        self, **kwargs: Unpack[DeleteTableRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a given Timestream table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/delete_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#delete_table)
        """

    def describe_batch_load_task(
        self, **kwargs: Unpack[DescribeBatchLoadTaskRequestTypeDef]
    ) -> DescribeBatchLoadTaskResponseTypeDef:
        """
        Returns information about the batch load task, including configurations,
        mappings, progress, and other details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/describe_batch_load_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#describe_batch_load_task)
        """

    def describe_database(
        self, **kwargs: Unpack[DescribeDatabaseRequestTypeDef]
    ) -> DescribeDatabaseResponseTypeDef:
        """
        Returns information about the database, including the database name, time that
        the database was created, and the total number of tables found within the
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/describe_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#describe_database)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        Returns a list of available endpoints to make Timestream API calls against.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/describe_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#describe_endpoints)
        """

    def describe_table(
        self, **kwargs: Unpack[DescribeTableRequestTypeDef]
    ) -> DescribeTableResponseTypeDef:
        """
        Returns information about the table, including the table name, database name,
        retention duration of the memory store and the magnetic store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/describe_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#describe_table)
        """

    def list_batch_load_tasks(
        self, **kwargs: Unpack[ListBatchLoadTasksRequestTypeDef]
    ) -> ListBatchLoadTasksResponseTypeDef:
        """
        Provides a list of batch load tasks, along with the name, status, when the task
        is resumable until, and other details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/list_batch_load_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#list_batch_load_tasks)
        """

    def list_databases(
        self, **kwargs: Unpack[ListDatabasesRequestTypeDef]
    ) -> ListDatabasesResponseTypeDef:
        """
        Returns a list of your Timestream databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/list_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#list_databases)
        """

    def list_tables(self, **kwargs: Unpack[ListTablesRequestTypeDef]) -> ListTablesResponseTypeDef:
        """
        Provides a list of tables, along with the name, status, and retention
        properties of each table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/list_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#list_tables)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on a Timestream resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#list_tags_for_resource)
        """

    def resume_batch_load_task(
        self, **kwargs: Unpack[ResumeBatchLoadTaskRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/resume_batch_load_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#resume_batch_load_task)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates a set of tags with a Timestream resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the association of tags from a Timestream resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#untag_resource)
        """

    def update_database(
        self, **kwargs: Unpack[UpdateDatabaseRequestTypeDef]
    ) -> UpdateDatabaseResponseTypeDef:
        """
        Modifies the KMS key for an existing database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/update_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#update_database)
        """

    def update_table(
        self, **kwargs: Unpack[UpdateTableRequestTypeDef]
    ) -> UpdateTableResponseTypeDef:
        """
        Modifies the retention duration of the memory store and magnetic store for your
        Timestream table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/update_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#update_table)
        """

    def write_records(
        self, **kwargs: Unpack[WriteRecordsRequestTypeDef]
    ) -> WriteRecordsResponseTypeDef:
        """
        Enables you to write your time-series data into Timestream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write/client/write_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client/#write_records)
        """
