"""
Type annotations for artifact service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_artifact import ArtifactClient

    client: ArtifactClient = boto3.client("artifact")
    ```
"""

import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import NotificationSubscriptionStatusType
from .paginator import ListReportsPaginator
from .type_defs import (
    GetAccountSettingsResponseTypeDef,
    GetReportMetadataResponseTypeDef,
    GetReportResponseTypeDef,
    GetTermForReportResponseTypeDef,
    ListReportsResponseTypeDef,
    PutAccountSettingsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ArtifactClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ArtifactClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ArtifactClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#generate_presigned_url)
        """

    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        Get the account settings for Artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#get_account_settings)
        """

    def get_report(
        self, *, reportId: str, termToken: str, reportVersion: int = None
    ) -> GetReportResponseTypeDef:
        """
        Get the content for a single report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.get_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#get_report)
        """

    def get_report_metadata(
        self, *, reportId: str, reportVersion: int = None
    ) -> GetReportMetadataResponseTypeDef:
        """
        Get the metadata for a single report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.get_report_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#get_report_metadata)
        """

    def get_term_for_report(
        self, *, reportId: str, reportVersion: int = None
    ) -> GetTermForReportResponseTypeDef:
        """
        Get the Term content associated with a single report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.get_term_for_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#get_term_for_report)
        """

    def list_reports(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListReportsResponseTypeDef:
        """
        List available reports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.list_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#list_reports)
        """

    def put_account_settings(
        self, *, notificationSubscriptionStatus: NotificationSubscriptionStatusType = None
    ) -> PutAccountSettingsResponseTypeDef:
        """
        Put the account settings for Artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Client.put_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/client.html#put_account_settings)
        """

    def get_paginator(self, operation_name: Literal["list_reports"]) -> ListReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Paginator.ListReports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators.html#listreportspaginator)
        """
