# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for timestream-write service client

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_write import TimestreamWriteClient

    client: TimestreamWriteClient = boto3.client("timestream-write")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_timestream_write.type_defs import (
    CreateDatabaseResponseTypeDef,
    CreateTableResponseTypeDef,
    DescribeDatabaseResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeTableResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RecordTypeDef,
    RetentionPropertiesTypeDef,
    TagTypeDef,
    UpdateDatabaseResponseTypeDef,
    UpdateTableResponseTypeDef,
)

__all__ = ("TimestreamWriteClient",)


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
    InvalidEndpointException: Type[BotocoreClientError]
    RejectedRecordsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class TimestreamWriteClient:
    """
    [TimestreamWrite.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.can_paginate)
        """

    def create_database(
        self, DatabaseName: str, KmsKeyId: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateDatabaseResponseTypeDef:
        """
        [Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.create_database)
        """

    def create_table(
        self,
        DatabaseName: str,
        TableName: str,
        RetentionProperties: "RetentionPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTableResponseTypeDef:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.create_table)
        """

    def delete_database(self, DatabaseName: str) -> None:
        """
        [Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.delete_database)
        """

    def delete_table(self, DatabaseName: str, TableName: str) -> None:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.delete_table)
        """

    def describe_database(self, DatabaseName: str) -> DescribeDatabaseResponseTypeDef:
        """
        [Client.describe_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.describe_database)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.describe_endpoints)
        """

    def describe_table(self, DatabaseName: str, TableName: str) -> DescribeTableResponseTypeDef:
        """
        [Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.describe_table)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.generate_presigned_url)
        """

    def list_databases(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatabasesResponseTypeDef:
        """
        [Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.list_databases)
        """

    def list_tables(
        self, DatabaseName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListTablesResponseTypeDef:
        """
        [Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.list_tables)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.untag_resource)
        """

    def update_database(self, DatabaseName: str, KmsKeyId: str) -> UpdateDatabaseResponseTypeDef:
        """
        [Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.update_database)
        """

    def update_table(
        self, DatabaseName: str, TableName: str, RetentionProperties: "RetentionPropertiesTypeDef"
    ) -> UpdateTableResponseTypeDef:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.update_table)
        """

    def write_records(
        self,
        DatabaseName: str,
        TableName: str,
        Records: List[RecordTypeDef],
        CommonAttributes: RecordTypeDef = None,
    ) -> None:
        """
        [Client.write_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-write.html#TimestreamWrite.Client.write_records)
        """
