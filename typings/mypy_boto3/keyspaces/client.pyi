"""
Type annotations for keyspaces service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_keyspaces import KeyspacesClient

    client: KeyspacesClient = boto3.client("keyspaces")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListKeyspacesPaginator, ListTablesPaginator, ListTagsForResourcePaginator
from .type_defs import (
    CapacitySpecificationTypeDef,
    ClientSideTimestampsTypeDef,
    ColumnDefinitionTypeDef,
    CommentTypeDef,
    CreateKeyspaceResponseTypeDef,
    CreateTableResponseTypeDef,
    EncryptionSpecificationTypeDef,
    GetKeyspaceResponseTypeDef,
    GetTableResponseTypeDef,
    ListKeyspacesResponseTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PointInTimeRecoveryTypeDef,
    ReplicationSpecificationTypeDef,
    RestoreTableResponseTypeDef,
    SchemaDefinitionTypeDef,
    TagTypeDef,
    TimeToLiveTypeDef,
    UpdateTableResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KeyspacesClient",)

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
    ValidationException: Type[BotocoreClientError]

class KeyspacesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KeyspacesClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#close)
        """
    def create_keyspace(
        self,
        *,
        keyspaceName: str,
        tags: List["TagTypeDef"] = None,
        replicationSpecification: "ReplicationSpecificationTypeDef" = None
    ) -> CreateKeyspaceResponseTypeDef:
        """
        The `CreateKeyspace` operation adds a new keyspace to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.create_keyspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#create_keyspace)
        """
    def create_table(
        self,
        *,
        keyspaceName: str,
        tableName: str,
        schemaDefinition: "SchemaDefinitionTypeDef",
        comment: "CommentTypeDef" = None,
        capacitySpecification: "CapacitySpecificationTypeDef" = None,
        encryptionSpecification: "EncryptionSpecificationTypeDef" = None,
        pointInTimeRecovery: "PointInTimeRecoveryTypeDef" = None,
        ttl: "TimeToLiveTypeDef" = None,
        defaultTimeToLive: int = None,
        tags: List["TagTypeDef"] = None,
        clientSideTimestamps: "ClientSideTimestampsTypeDef" = None
    ) -> CreateTableResponseTypeDef:
        """
        The `CreateTable` operation adds a new table to the specified keyspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.create_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#create_table)
        """
    def delete_keyspace(self, *, keyspaceName: str) -> Dict[str, Any]:
        """
        The `DeleteKeyspace` operation deletes a keyspace and all of its tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.delete_keyspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#delete_keyspace)
        """
    def delete_table(self, *, keyspaceName: str, tableName: str) -> Dict[str, Any]:
        """
        The `DeleteTable` operation deletes a table and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.delete_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#delete_table)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#generate_presigned_url)
        """
    def get_keyspace(self, *, keyspaceName: str) -> GetKeyspaceResponseTypeDef:
        """
        Returns the name and the Amazon Resource Name (ARN) of the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.get_keyspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#get_keyspace)
        """
    def get_table(self, *, keyspaceName: str, tableName: str) -> GetTableResponseTypeDef:
        """
        Returns information about the table, including the table's name and current
        status, the keyspace name, configuration settings, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.get_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#get_table)
        """
    def list_keyspaces(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListKeyspacesResponseTypeDef:
        """
        Returns a list of keyspaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.list_keyspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#list_keyspaces)
        """
    def list_tables(
        self, *, keyspaceName: str, nextToken: str = None, maxResults: int = None
    ) -> ListTablesResponseTypeDef:
        """
        Returns a list of tables for a specified keyspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#list_tables)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all tags associated with the specified Amazon Keyspaces
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#list_tags_for_resource)
        """
    def restore_table(
        self,
        *,
        sourceKeyspaceName: str,
        sourceTableName: str,
        targetKeyspaceName: str,
        targetTableName: str,
        restoreTimestamp: Union[datetime, str] = None,
        capacitySpecificationOverride: "CapacitySpecificationTypeDef" = None,
        encryptionSpecificationOverride: "EncryptionSpecificationTypeDef" = None,
        pointInTimeRecoveryOverride: "PointInTimeRecoveryTypeDef" = None,
        tagsOverride: List["TagTypeDef"] = None
    ) -> RestoreTableResponseTypeDef:
        """
        Restores the specified table to the specified point in time within the
        `earliest_restorable_timestamp` and the current time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.restore_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#restore_table)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates a set of tags with a Amazon Keyspaces resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Removes the association of tags from a Amazon Keyspaces resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#untag_resource)
        """
    def update_table(
        self,
        *,
        keyspaceName: str,
        tableName: str,
        addColumns: List["ColumnDefinitionTypeDef"] = None,
        capacitySpecification: "CapacitySpecificationTypeDef" = None,
        encryptionSpecification: "EncryptionSpecificationTypeDef" = None,
        pointInTimeRecovery: "PointInTimeRecoveryTypeDef" = None,
        ttl: "TimeToLiveTypeDef" = None,
        defaultTimeToLive: int = None,
        clientSideTimestamps: "ClientSideTimestampsTypeDef" = None
    ) -> UpdateTableResponseTypeDef:
        """
        Adds new columns to the table or updates one of the table's settings, for
        example capacity mode, encryption, point-in-time recovery, or ttl settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Client.update_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/client.html#update_table)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_keyspaces"]) -> ListKeyspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Paginator.ListKeyspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators.html#listkeyspacespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Paginator.ListTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators.html#listtablespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/keyspaces.html#Keyspaces.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/paginators.html#listtagsforresourcepaginator)
        """
