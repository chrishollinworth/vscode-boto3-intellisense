"""
Type annotations for codeguru-security service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_security import CodeGuruSecurityClient

    client: CodeGuruSecurityClient = boto3.client("codeguru-security")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AnalysisTypeType, ScanTypeType, StatusType
from .paginator import GetFindingsPaginator, ListFindingsMetricsPaginator, ListScansPaginator
from .type_defs import (
    BatchGetFindingsResponseTypeDef,
    CreateScanResponseTypeDef,
    CreateUploadUrlResponseTypeDef,
    EncryptionConfigTypeDef,
    FindingIdentifierTypeDef,
    GetAccountConfigurationResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetMetricsSummaryResponseTypeDef,
    GetScanResponseTypeDef,
    ListFindingsMetricsResponseTypeDef,
    ListScansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResourceIdTypeDef,
    UpdateAccountConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeGuruSecurityClient",)

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

class CodeGuruSecurityClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeGuruSecurityClient exceptions.
        """

    def batch_get_findings(
        self, *, findingIdentifiers: List["FindingIdentifierTypeDef"]
    ) -> BatchGetFindingsResponseTypeDef:
        """
        Returns a list of requested findings from standard scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.batch_get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#batch_get_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#close)
        """

    def create_scan(
        self,
        *,
        resourceId: "ResourceIdTypeDef",
        scanName: str,
        analysisType: AnalysisTypeType = None,
        clientToken: str = None,
        scanType: ScanTypeType = None,
        tags: Dict[str, str] = None
    ) -> CreateScanResponseTypeDef:
        """
        Use to create a scan using code uploaded to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.create_scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#create_scan)
        """

    def create_upload_url(self, *, scanName: str) -> CreateUploadUrlResponseTypeDef:
        """
        Generates a pre-signed URL, request headers used to upload a code resource, and
        code artifact identifier for the uploaded resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.create_upload_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#create_upload_url)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#generate_presigned_url)
        """

    def get_account_configuration(self) -> GetAccountConfigurationResponseTypeDef:
        """
        Use to get the encryption configuration for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.get_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#get_account_configuration)
        """

    def get_findings(
        self,
        *,
        scanName: str,
        maxResults: int = None,
        nextToken: str = None,
        status: StatusType = None
    ) -> GetFindingsResponseTypeDef:
        """
        Returns a list of all findings generated by a particular scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#get_findings)
        """

    def get_metrics_summary(
        self, *, date: Union[datetime, str]
    ) -> GetMetricsSummaryResponseTypeDef:
        """
        Returns a summary of metrics for an account from a specified date, including
        number of open findings, the categories with most findings, the scans with most
        open findings, and scans with most open critical findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.get_metrics_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#get_metrics_summary)
        """

    def get_scan(self, *, scanName: str, runId: str = None) -> GetScanResponseTypeDef:
        """
        Returns details about a scan, including whether or not a scan has completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.get_scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#get_scan)
        """

    def list_findings_metrics(
        self,
        *,
        endDate: Union[datetime, str],
        startDate: Union[datetime, str],
        maxResults: int = None,
        nextToken: str = None
    ) -> ListFindingsMetricsResponseTypeDef:
        """
        Returns metrics about all findings in an account within a specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.list_findings_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#list_findings_metrics)
        """

    def list_scans(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListScansResponseTypeDef:
        """
        Returns a list of all scans in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.list_scans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#list_scans)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all tags associated with a scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Use to add one or more tags to an existing scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Use to remove one or more tags from an existing scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#untag_resource)
        """

    def update_account_configuration(
        self, *, encryptionConfig: "EncryptionConfigTypeDef"
    ) -> UpdateAccountConfigurationResponseTypeDef:
        """
        Use to update the encryption configuration for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Client.update_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client.html#update_account_configuration)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_findings"]) -> GetFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.GetFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#getfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_findings_metrics"]
    ) -> ListFindingsMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListFindingsMetrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listfindingsmetricspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_scans"]) -> ListScansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListScans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listscanspaginator)
        """
