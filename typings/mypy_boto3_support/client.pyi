"""
Type annotations for support service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_support.client import SupportClient

    session = Session()
    client: SupportClient = session.client("support")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator
from .type_defs import (
    AddAttachmentsToSetRequestTypeDef,
    AddAttachmentsToSetResponseTypeDef,
    AddCommunicationToCaseRequestTypeDef,
    AddCommunicationToCaseResponseTypeDef,
    CreateCaseRequestTypeDef,
    CreateCaseResponseTypeDef,
    DescribeAttachmentRequestTypeDef,
    DescribeAttachmentResponseTypeDef,
    DescribeCasesRequestTypeDef,
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsRequestTypeDef,
    DescribeCommunicationsResponseTypeDef,
    DescribeCreateCaseOptionsRequestTypeDef,
    DescribeCreateCaseOptionsResponseTypeDef,
    DescribeServicesRequestTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeSeverityLevelsRequestTypeDef,
    DescribeSeverityLevelsResponseTypeDef,
    DescribeSupportedLanguagesRequestTypeDef,
    DescribeSupportedLanguagesResponseTypeDef,
    DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef,
    DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef,
    DescribeTrustedAdvisorCheckResultRequestTypeDef,
    DescribeTrustedAdvisorCheckResultResponseTypeDef,
    DescribeTrustedAdvisorChecksRequestTypeDef,
    DescribeTrustedAdvisorChecksResponseTypeDef,
    DescribeTrustedAdvisorCheckSummariesRequestTypeDef,
    DescribeTrustedAdvisorCheckSummariesResponseTypeDef,
    RefreshTrustedAdvisorCheckRequestTypeDef,
    RefreshTrustedAdvisorCheckResponseTypeDef,
    ResolveCaseRequestTypeDef,
    ResolveCaseResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SupportClient",)

class Exceptions(BaseClientExceptions):
    AttachmentIdNotFound: Type[BotocoreClientError]
    AttachmentLimitExceeded: Type[BotocoreClientError]
    AttachmentSetExpired: Type[BotocoreClientError]
    AttachmentSetIdNotFound: Type[BotocoreClientError]
    AttachmentSetSizeLimitExceeded: Type[BotocoreClientError]
    CaseCreationLimitExceeded: Type[BotocoreClientError]
    CaseIdNotFound: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DescribeAttachmentLimitExceeded: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class SupportClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SupportClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#generate_presigned_url)
        """

    def add_attachments_to_set(
        self, **kwargs: Unpack[AddAttachmentsToSetRequestTypeDef]
    ) -> AddAttachmentsToSetResponseTypeDef:
        """
        Adds one or more attachments to an attachment set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/add_attachments_to_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#add_attachments_to_set)
        """

    def add_communication_to_case(
        self, **kwargs: Unpack[AddCommunicationToCaseRequestTypeDef]
    ) -> AddCommunicationToCaseResponseTypeDef:
        """
        Adds additional customer communication to an Amazon Web Services Support case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/add_communication_to_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#add_communication_to_case)
        """

    def create_case(self, **kwargs: Unpack[CreateCaseRequestTypeDef]) -> CreateCaseResponseTypeDef:
        """
        Creates a case in the Amazon Web Services Support Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/create_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#create_case)
        """

    def describe_attachment(
        self, **kwargs: Unpack[DescribeAttachmentRequestTypeDef]
    ) -> DescribeAttachmentResponseTypeDef:
        """
        Returns the attachment that has the specified ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_attachment)
        """

    def describe_cases(
        self, **kwargs: Unpack[DescribeCasesRequestTypeDef]
    ) -> DescribeCasesResponseTypeDef:
        """
        Returns a list of cases that you specify by passing one or more case IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_cases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_cases)
        """

    def describe_communications(
        self, **kwargs: Unpack[DescribeCommunicationsRequestTypeDef]
    ) -> DescribeCommunicationsResponseTypeDef:
        """
        Returns communications and attachments for one or more support cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_communications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_communications)
        """

    def describe_create_case_options(
        self, **kwargs: Unpack[DescribeCreateCaseOptionsRequestTypeDef]
    ) -> DescribeCreateCaseOptionsResponseTypeDef:
        """
        Returns a list of CreateCaseOption types along with the corresponding supported
        hours and language availability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_create_case_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_create_case_options)
        """

    def describe_services(
        self, **kwargs: Unpack[DescribeServicesRequestTypeDef]
    ) -> DescribeServicesResponseTypeDef:
        """
        Returns the current list of Amazon Web Services services and a list of service
        categories for each service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_services)
        """

    def describe_severity_levels(
        self, **kwargs: Unpack[DescribeSeverityLevelsRequestTypeDef]
    ) -> DescribeSeverityLevelsResponseTypeDef:
        """
        Returns the list of severity levels that you can assign to a support case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_severity_levels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_severity_levels)
        """

    def describe_supported_languages(
        self, **kwargs: Unpack[DescribeSupportedLanguagesRequestTypeDef]
    ) -> DescribeSupportedLanguagesResponseTypeDef:
        """
        Returns a list of supported languages for a specified
        <code>categoryCode</code>, <code>issueType</code> and <code>serviceCode</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_supported_languages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_supported_languages)
        """

    def describe_trusted_advisor_check_refresh_statuses(
        self, **kwargs: Unpack[DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef]
    ) -> DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
        """
        Returns the refresh status of the Trusted Advisor checks that have the
        specified check IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_trusted_advisor_check_refresh_statuses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_trusted_advisor_check_refresh_statuses)
        """

    def describe_trusted_advisor_check_result(
        self, **kwargs: Unpack[DescribeTrustedAdvisorCheckResultRequestTypeDef]
    ) -> DescribeTrustedAdvisorCheckResultResponseTypeDef:
        """
        Returns the results of the Trusted Advisor check that has the specified check
        ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_trusted_advisor_check_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_trusted_advisor_check_result)
        """

    def describe_trusted_advisor_check_summaries(
        self, **kwargs: Unpack[DescribeTrustedAdvisorCheckSummariesRequestTypeDef]
    ) -> DescribeTrustedAdvisorCheckSummariesResponseTypeDef:
        """
        Returns the results for the Trusted Advisor check summaries for the check IDs
        that you specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_trusted_advisor_check_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_trusted_advisor_check_summaries)
        """

    def describe_trusted_advisor_checks(
        self, **kwargs: Unpack[DescribeTrustedAdvisorChecksRequestTypeDef]
    ) -> DescribeTrustedAdvisorChecksResponseTypeDef:
        """
        Returns information about all available Trusted Advisor checks, including the
        name, ID, category, description, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/describe_trusted_advisor_checks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#describe_trusted_advisor_checks)
        """

    def refresh_trusted_advisor_check(
        self, **kwargs: Unpack[RefreshTrustedAdvisorCheckRequestTypeDef]
    ) -> RefreshTrustedAdvisorCheckResponseTypeDef:
        """
        Refreshes the Trusted Advisor check that you specify using the check ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/refresh_trusted_advisor_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#refresh_trusted_advisor_check)
        """

    def resolve_case(
        self, **kwargs: Unpack[ResolveCaseRequestTypeDef]
    ) -> ResolveCaseResponseTypeDef:
        """
        Resolves a support case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/resolve_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#resolve_case)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cases"]
    ) -> DescribeCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_communications"]
    ) -> DescribeCommunicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/client/#get_paginator)
        """
