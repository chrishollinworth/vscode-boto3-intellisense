"""
Type annotations for codeguru-security service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeguru_security.client import CodeGuruSecurityClient

    session = Session()
    client: CodeGuruSecurityClient = session.client("codeguru-security")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import GetFindingsPaginator, ListFindingsMetricsPaginator, ListScansPaginator
from .type_defs import (
    BatchGetFindingsRequestTypeDef,
    BatchGetFindingsResponseTypeDef,
    CreateScanRequestTypeDef,
    CreateScanResponseTypeDef,
    CreateUploadUrlRequestTypeDef,
    CreateUploadUrlResponseTypeDef,
    GetAccountConfigurationResponseTypeDef,
    GetFindingsRequestTypeDef,
    GetFindingsResponseTypeDef,
    GetMetricsSummaryRequestTypeDef,
    GetMetricsSummaryResponseTypeDef,
    GetScanRequestTypeDef,
    GetScanResponseTypeDef,
    ListFindingsMetricsRequestTypeDef,
    ListFindingsMetricsResponseTypeDef,
    ListScansRequestTypeDef,
    ListScansResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccountConfigurationRequestTypeDef,
    UpdateAccountConfigurationResponseTypeDef,
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

__all__ = ("CodeGuruSecurityClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeGuruSecurityClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security.html#CodeGuruSecurity.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeGuruSecurityClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security.html#CodeGuruSecurity.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#generate_presigned_url)
        """

    def batch_get_findings(
        self, **kwargs: Unpack[BatchGetFindingsRequestTypeDef]
    ) -> BatchGetFindingsResponseTypeDef:
        """
        Returns a list of requested findings from standard scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/batch_get_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#batch_get_findings)
        """

    def create_scan(self, **kwargs: Unpack[CreateScanRequestTypeDef]) -> CreateScanResponseTypeDef:
        """
        Use to create a scan using code uploaded to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/create_scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#create_scan)
        """

    def create_upload_url(
        self, **kwargs: Unpack[CreateUploadUrlRequestTypeDef]
    ) -> CreateUploadUrlResponseTypeDef:
        """
        Generates a pre-signed URL, request headers used to upload a code resource, and
        code artifact identifier for the uploaded resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/create_upload_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#create_upload_url)
        """

    def get_account_configuration(self) -> GetAccountConfigurationResponseTypeDef:
        """
        Use to get the encryption configuration for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_account_configuration)
        """

    def get_findings(
        self, **kwargs: Unpack[GetFindingsRequestTypeDef]
    ) -> GetFindingsResponseTypeDef:
        """
        Returns a list of all findings generated by a particular scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_findings)
        """

    def get_metrics_summary(
        self, **kwargs: Unpack[GetMetricsSummaryRequestTypeDef]
    ) -> GetMetricsSummaryResponseTypeDef:
        """
        Returns a summary of metrics for an account from a specified date, including
        number of open findings, the categories with most findings, the scans with most
        open findings, and scans with most open critical findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_metrics_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_metrics_summary)
        """

    def get_scan(self, **kwargs: Unpack[GetScanRequestTypeDef]) -> GetScanResponseTypeDef:
        """
        Returns details about a scan, including whether or not a scan has completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_scan)
        """

    def list_findings_metrics(
        self, **kwargs: Unpack[ListFindingsMetricsRequestTypeDef]
    ) -> ListFindingsMetricsResponseTypeDef:
        """
        Returns metrics about all findings in an account within a specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/list_findings_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#list_findings_metrics)
        """

    def list_scans(self, **kwargs: Unpack[ListScansRequestTypeDef]) -> ListScansResponseTypeDef:
        """
        Returns a list of all scans in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/list_scans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#list_scans)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all tags associated with a scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Use to add one or more tags to an existing scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Use to remove one or more tags from an existing scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#untag_resource)
        """

    def update_account_configuration(
        self, **kwargs: Unpack[UpdateAccountConfigurationRequestTypeDef]
    ) -> UpdateAccountConfigurationResponseTypeDef:
        """
        Use to update the encryption configuration for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/update_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#update_account_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_findings"]
    ) -> GetFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_findings_metrics"]
    ) -> ListFindingsMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scans"]
    ) -> ListScansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/client/#get_paginator)
        """
