"""
Type annotations for qldb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb import QLDBClient

    client: QLDBClient = boto3.client("qldb")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import OutputFormatType, PermissionsModeType
from .type_defs import (
    CancelJournalKinesisStreamResponseTypeDef,
    CreateLedgerResponseTypeDef,
    DescribeJournalKinesisStreamResponseTypeDef,
    DescribeJournalS3ExportResponseTypeDef,
    DescribeLedgerResponseTypeDef,
    ExportJournalToS3ResponseTypeDef,
    GetBlockResponseTypeDef,
    GetDigestResponseTypeDef,
    GetRevisionResponseTypeDef,
    KinesisConfigurationTypeDef,
    ListJournalKinesisStreamsForLedgerResponseTypeDef,
    ListJournalS3ExportsForLedgerResponseTypeDef,
    ListJournalS3ExportsResponseTypeDef,
    ListLedgersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    S3ExportConfigurationTypeDef,
    StreamJournalToKinesisResponseTypeDef,
    UpdateLedgerPermissionsModeResponseTypeDef,
    UpdateLedgerResponseTypeDef,
    ValueHolderTypeDef,
)

__all__ = ("QLDBClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePreconditionNotMetException: Type[BotocoreClientError]

class QLDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QLDBClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#can_paginate)
        """
    def cancel_journal_kinesis_stream(
        self, *, LedgerName: str, StreamId: str
    ) -> CancelJournalKinesisStreamResponseTypeDef:
        """
        Ends a given Amazon QLDB journal stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.cancel_journal_kinesis_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#cancel_journal_kinesis_stream)
        """
    def create_ledger(
        self,
        *,
        Name: str,
        PermissionsMode: PermissionsModeType,
        Tags: Dict[str, str] = None,
        DeletionProtection: bool = None,
        KmsKey: str = None
    ) -> CreateLedgerResponseTypeDef:
        """
        Creates a new ledger in your Amazon Web Services account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.create_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#create_ledger)
        """
    def delete_ledger(self, *, Name: str) -> None:
        """
        Deletes a ledger and all of its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.delete_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#delete_ledger)
        """
    def describe_journal_kinesis_stream(
        self, *, LedgerName: str, StreamId: str
    ) -> DescribeJournalKinesisStreamResponseTypeDef:
        """
        Returns detailed information about a given Amazon QLDB journal stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.describe_journal_kinesis_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#describe_journal_kinesis_stream)
        """
    def describe_journal_s3_export(
        self, *, Name: str, ExportId: str
    ) -> DescribeJournalS3ExportResponseTypeDef:
        """
        Returns information about a journal export job, including the ledger name,
        export ID, creation time, current status, and the parameters of the original
        export creation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.describe_journal_s3_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#describe_journal_s3_export)
        """
    def describe_ledger(self, *, Name: str) -> DescribeLedgerResponseTypeDef:
        """
        Returns information about a ledger, including its state, permissions mode,
        encryption at rest settings, and when it was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.describe_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#describe_ledger)
        """
    def export_journal_to_s3(
        self,
        *,
        Name: str,
        InclusiveStartTime: Union[datetime, str],
        ExclusiveEndTime: Union[datetime, str],
        S3ExportConfiguration: "S3ExportConfigurationTypeDef",
        RoleArn: str,
        OutputFormat: OutputFormatType = None
    ) -> ExportJournalToS3ResponseTypeDef:
        """
        Exports journal contents within a date and time range from a ledger into a
        specified Amazon Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.export_journal_to_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#export_journal_to_s3)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#generate_presigned_url)
        """
    def get_block(
        self,
        *,
        Name: str,
        BlockAddress: "ValueHolderTypeDef",
        DigestTipAddress: "ValueHolderTypeDef" = None
    ) -> GetBlockResponseTypeDef:
        """
        Returns a block object at a specified address in a journal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.get_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#get_block)
        """
    def get_digest(self, *, Name: str) -> GetDigestResponseTypeDef:
        """
        Returns the digest of a ledger at the latest committed block in the journal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.get_digest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#get_digest)
        """
    def get_revision(
        self,
        *,
        Name: str,
        BlockAddress: "ValueHolderTypeDef",
        DocumentId: str,
        DigestTipAddress: "ValueHolderTypeDef" = None
    ) -> GetRevisionResponseTypeDef:
        """
        Returns a revision data object for a specified document ID and block address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.get_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#get_revision)
        """
    def list_journal_kinesis_streams_for_ledger(
        self, *, LedgerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalKinesisStreamsForLedgerResponseTypeDef:
        """
        Returns an array of all Amazon QLDB journal stream descriptors for a given
        ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.list_journal_kinesis_streams_for_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#list_journal_kinesis_streams_for_ledger)
        """
    def list_journal_s3_exports(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalS3ExportsResponseTypeDef:
        """
        Returns an array of journal export job descriptions for all ledgers that are
        associated with the current Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#list_journal_s3_exports)
        """
    def list_journal_s3_exports_for_ledger(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalS3ExportsForLedgerResponseTypeDef:
        """
        Returns an array of journal export job descriptions for a specified ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports_for_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#list_journal_s3_exports_for_ledger)
        """
    def list_ledgers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListLedgersResponseTypeDef:
        """
        Returns an array of ledger summaries that are associated with the current Amazon
        Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.list_ledgers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#list_ledgers)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all tags for a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#list_tags_for_resource)
        """
    def stream_journal_to_kinesis(
        self,
        *,
        LedgerName: str,
        RoleArn: str,
        InclusiveStartTime: Union[datetime, str],
        KinesisConfiguration: "KinesisConfigurationTypeDef",
        StreamName: str,
        Tags: Dict[str, str] = None,
        ExclusiveEndTime: Union[datetime, str] = None
    ) -> StreamJournalToKinesisResponseTypeDef:
        """
        Creates a journal stream for a given Amazon QLDB ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.stream_journal_to_kinesis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#stream_journal_to_kinesis)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#untag_resource)
        """
    def update_ledger(
        self, *, Name: str, DeletionProtection: bool = None, KmsKey: str = None
    ) -> UpdateLedgerResponseTypeDef:
        """
        Updates properties on a ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.update_ledger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#update_ledger)
        """
    def update_ledger_permissions_mode(
        self, *, Name: str, PermissionsMode: PermissionsModeType
    ) -> UpdateLedgerPermissionsModeResponseTypeDef:
        """
        Updates the permissions mode of a ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/qldb.html#QLDB.Client.update_ledger_permissions_mode)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/client.html#update_ledger_permissions_mode)
        """
