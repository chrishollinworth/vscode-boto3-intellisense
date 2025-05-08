"""
Type annotations for qldb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qldb.client import QLDBClient

    session = Session()
    client: QLDBClient = session.client("qldb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CancelJournalKinesisStreamRequestTypeDef,
    CancelJournalKinesisStreamResponseTypeDef,
    CreateLedgerRequestTypeDef,
    CreateLedgerResponseTypeDef,
    DeleteLedgerRequestTypeDef,
    DescribeJournalKinesisStreamRequestTypeDef,
    DescribeJournalKinesisStreamResponseTypeDef,
    DescribeJournalS3ExportRequestTypeDef,
    DescribeJournalS3ExportResponseTypeDef,
    DescribeLedgerRequestTypeDef,
    DescribeLedgerResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportJournalToS3RequestTypeDef,
    ExportJournalToS3ResponseTypeDef,
    GetBlockRequestTypeDef,
    GetBlockResponseTypeDef,
    GetDigestRequestTypeDef,
    GetDigestResponseTypeDef,
    GetRevisionRequestTypeDef,
    GetRevisionResponseTypeDef,
    ListJournalKinesisStreamsForLedgerRequestTypeDef,
    ListJournalKinesisStreamsForLedgerResponseTypeDef,
    ListJournalS3ExportsForLedgerRequestTypeDef,
    ListJournalS3ExportsForLedgerResponseTypeDef,
    ListJournalS3ExportsRequestTypeDef,
    ListJournalS3ExportsResponseTypeDef,
    ListLedgersRequestTypeDef,
    ListLedgersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StreamJournalToKinesisRequestTypeDef,
    StreamJournalToKinesisResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLedgerPermissionsModeRequestTypeDef,
    UpdateLedgerPermissionsModeResponseTypeDef,
    UpdateLedgerRequestTypeDef,
    UpdateLedgerResponseTypeDef,
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

__all__ = ("QLDBClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePreconditionNotMetException: Type[BotocoreClientError]

class QLDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QLDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#generate_presigned_url)
        """

    def cancel_journal_kinesis_stream(
        self, **kwargs: Unpack[CancelJournalKinesisStreamRequestTypeDef]
    ) -> CancelJournalKinesisStreamResponseTypeDef:
        """
        Ends a given Amazon QLDB journal stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/cancel_journal_kinesis_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#cancel_journal_kinesis_stream)
        """

    def create_ledger(
        self, **kwargs: Unpack[CreateLedgerRequestTypeDef]
    ) -> CreateLedgerResponseTypeDef:
        """
        Creates a new ledger in your Amazon Web Services account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/create_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#create_ledger)
        """

    def delete_ledger(
        self, **kwargs: Unpack[DeleteLedgerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a ledger and all of its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/delete_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#delete_ledger)
        """

    def describe_journal_kinesis_stream(
        self, **kwargs: Unpack[DescribeJournalKinesisStreamRequestTypeDef]
    ) -> DescribeJournalKinesisStreamResponseTypeDef:
        """
        Returns detailed information about a given Amazon QLDB journal stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/describe_journal_kinesis_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#describe_journal_kinesis_stream)
        """

    def describe_journal_s3_export(
        self, **kwargs: Unpack[DescribeJournalS3ExportRequestTypeDef]
    ) -> DescribeJournalS3ExportResponseTypeDef:
        """
        Returns information about a journal export job, including the ledger name,
        export ID, creation time, current status, and the parameters of the original
        export creation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/describe_journal_s3_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#describe_journal_s3_export)
        """

    def describe_ledger(
        self, **kwargs: Unpack[DescribeLedgerRequestTypeDef]
    ) -> DescribeLedgerResponseTypeDef:
        """
        Returns information about a ledger, including its state, permissions mode,
        encryption at rest settings, and when it was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/describe_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#describe_ledger)
        """

    def export_journal_to_s3(
        self, **kwargs: Unpack[ExportJournalToS3RequestTypeDef]
    ) -> ExportJournalToS3ResponseTypeDef:
        """
        Exports journal contents within a date and time range from a ledger into a
        specified Amazon Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/export_journal_to_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#export_journal_to_s3)
        """

    def get_block(self, **kwargs: Unpack[GetBlockRequestTypeDef]) -> GetBlockResponseTypeDef:
        """
        Returns a block object at a specified address in a journal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/get_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#get_block)
        """

    def get_digest(self, **kwargs: Unpack[GetDigestRequestTypeDef]) -> GetDigestResponseTypeDef:
        """
        Returns the digest of a ledger at the latest committed block in the journal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/get_digest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#get_digest)
        """

    def get_revision(
        self, **kwargs: Unpack[GetRevisionRequestTypeDef]
    ) -> GetRevisionResponseTypeDef:
        """
        Returns a revision data object for a specified document ID and block address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/get_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#get_revision)
        """

    def list_journal_kinesis_streams_for_ledger(
        self, **kwargs: Unpack[ListJournalKinesisStreamsForLedgerRequestTypeDef]
    ) -> ListJournalKinesisStreamsForLedgerResponseTypeDef:
        """
        Returns all Amazon QLDB journal streams for a given ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/list_journal_kinesis_streams_for_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#list_journal_kinesis_streams_for_ledger)
        """

    def list_journal_s3_exports(
        self, **kwargs: Unpack[ListJournalS3ExportsRequestTypeDef]
    ) -> ListJournalS3ExportsResponseTypeDef:
        """
        Returns all journal export jobs for all ledgers that are associated with the
        current Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/list_journal_s3_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#list_journal_s3_exports)
        """

    def list_journal_s3_exports_for_ledger(
        self, **kwargs: Unpack[ListJournalS3ExportsForLedgerRequestTypeDef]
    ) -> ListJournalS3ExportsForLedgerResponseTypeDef:
        """
        Returns all journal export jobs for a specified ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/list_journal_s3_exports_for_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#list_journal_s3_exports_for_ledger)
        """

    def list_ledgers(
        self, **kwargs: Unpack[ListLedgersRequestTypeDef]
    ) -> ListLedgersResponseTypeDef:
        """
        Returns all ledgers that are associated with the current Amazon Web Services
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/list_ledgers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#list_ledgers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all tags for a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#list_tags_for_resource)
        """

    def stream_journal_to_kinesis(
        self, **kwargs: Unpack[StreamJournalToKinesisRequestTypeDef]
    ) -> StreamJournalToKinesisResponseTypeDef:
        """
        Creates a journal stream for a given Amazon QLDB ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/stream_journal_to_kinesis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#stream_journal_to_kinesis)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified Amazon QLDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#untag_resource)
        """

    def update_ledger(
        self, **kwargs: Unpack[UpdateLedgerRequestTypeDef]
    ) -> UpdateLedgerResponseTypeDef:
        """
        Updates properties on a ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/update_ledger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#update_ledger)
        """

    def update_ledger_permissions_mode(
        self, **kwargs: Unpack[UpdateLedgerPermissionsModeRequestTypeDef]
    ) -> UpdateLedgerPermissionsModeResponseTypeDef:
        """
        Updates the permissions mode of a ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb/client/update_ledger_permissions_mode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/client/#update_ledger_permissions_mode)
        """
