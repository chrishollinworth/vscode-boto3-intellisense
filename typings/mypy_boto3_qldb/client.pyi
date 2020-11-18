# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for qldb service client

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb import QLDBClient

    client: QLDBClient = boto3.client("qldb")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_qldb.type_defs import (
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
    UpdateLedgerResponseTypeDef,
    ValueHolderTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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


class QLDBClient:
    """
    [QLDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.can_paginate)
        """

    def cancel_journal_kinesis_stream(
        self, LedgerName: str, StreamId: str
    ) -> CancelJournalKinesisStreamResponseTypeDef:
        """
        [Client.cancel_journal_kinesis_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.cancel_journal_kinesis_stream)
        """

    def create_ledger(
        self,
        Name: str,
        PermissionsMode: Literal["ALLOW_ALL"],
        Tags: Dict[str, str] = None,
        DeletionProtection: bool = None,
    ) -> CreateLedgerResponseTypeDef:
        """
        [Client.create_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.create_ledger)
        """

    def delete_ledger(self, Name: str) -> None:
        """
        [Client.delete_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.delete_ledger)
        """

    def describe_journal_kinesis_stream(
        self, LedgerName: str, StreamId: str
    ) -> DescribeJournalKinesisStreamResponseTypeDef:
        """
        [Client.describe_journal_kinesis_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.describe_journal_kinesis_stream)
        """

    def describe_journal_s3_export(
        self, Name: str, ExportId: str
    ) -> DescribeJournalS3ExportResponseTypeDef:
        """
        [Client.describe_journal_s3_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.describe_journal_s3_export)
        """

    def describe_ledger(self, Name: str) -> DescribeLedgerResponseTypeDef:
        """
        [Client.describe_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.describe_ledger)
        """

    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: "S3ExportConfigurationTypeDef",
        RoleArn: str,
    ) -> ExportJournalToS3ResponseTypeDef:
        """
        [Client.export_journal_to_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.export_journal_to_s3)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.generate_presigned_url)
        """

    def get_block(
        self,
        Name: str,
        BlockAddress: "ValueHolderTypeDef",
        DigestTipAddress: "ValueHolderTypeDef" = None,
    ) -> GetBlockResponseTypeDef:
        """
        [Client.get_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.get_block)
        """

    def get_digest(self, Name: str) -> GetDigestResponseTypeDef:
        """
        [Client.get_digest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.get_digest)
        """

    def get_revision(
        self,
        Name: str,
        BlockAddress: "ValueHolderTypeDef",
        DocumentId: str,
        DigestTipAddress: "ValueHolderTypeDef" = None,
    ) -> GetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.get_revision)
        """

    def list_journal_kinesis_streams_for_ledger(
        self, LedgerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalKinesisStreamsForLedgerResponseTypeDef:
        """
        [Client.list_journal_kinesis_streams_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.list_journal_kinesis_streams_for_ledger)
        """

    def list_journal_s3_exports(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalS3ExportsResponseTypeDef:
        """
        [Client.list_journal_s3_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports)
        """

    def list_journal_s3_exports_for_ledger(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJournalS3ExportsForLedgerResponseTypeDef:
        """
        [Client.list_journal_s3_exports_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports_for_ledger)
        """

    def list_ledgers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListLedgersResponseTypeDef:
        """
        [Client.list_ledgers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.list_ledgers)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.list_tags_for_resource)
        """

    def stream_journal_to_kinesis(
        self,
        LedgerName: str,
        RoleArn: str,
        InclusiveStartTime: datetime,
        KinesisConfiguration: "KinesisConfigurationTypeDef",
        StreamName: str,
        Tags: Dict[str, str] = None,
        ExclusiveEndTime: datetime = None,
    ) -> StreamJournalToKinesisResponseTypeDef:
        """
        [Client.stream_journal_to_kinesis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.stream_journal_to_kinesis)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.untag_resource)
        """

    def update_ledger(
        self, Name: str, DeletionProtection: bool = None
    ) -> UpdateLedgerResponseTypeDef:
        """
        [Client.update_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb.html#QLDB.Client.update_ledger)
        """
