# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for support service client

Usage::

    ```python
    import boto3
    from mypy_boto3_support import SupportClient

    client: SupportClient = boto3.client("support")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_support.paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator
from mypy_boto3_support.type_defs import (
    AddAttachmentsToSetResponseTypeDef,
    AddCommunicationToCaseResponseTypeDef,
    AttachmentTypeDef,
    CreateCaseResponseTypeDef,
    DescribeAttachmentResponseTypeDef,
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsResponseTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeSeverityLevelsResponseTypeDef,
    DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef,
    DescribeTrustedAdvisorCheckResultResponseTypeDef,
    DescribeTrustedAdvisorChecksResponseTypeDef,
    DescribeTrustedAdvisorCheckSummariesResponseTypeDef,
    RefreshTrustedAdvisorCheckResponseTypeDef,
    ResolveCaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SupportClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
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


class SupportClient:
    """
    [Support.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_attachments_to_set(
        self, attachments: List["AttachmentTypeDef"], attachmentSetId: str = None
    ) -> AddAttachmentsToSetResponseTypeDef:
        """
        [Client.add_attachments_to_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.add_attachments_to_set)
        """

    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: str = None,
        ccEmailAddresses: List[str] = None,
        attachmentSetId: str = None,
    ) -> AddCommunicationToCaseResponseTypeDef:
        """
        [Client.add_communication_to_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.add_communication_to_case)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.can_paginate)
        """

    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: str = None,
        severityCode: str = None,
        categoryCode: str = None,
        ccEmailAddresses: List[str] = None,
        language: str = None,
        issueType: str = None,
        attachmentSetId: str = None,
    ) -> CreateCaseResponseTypeDef:
        """
        [Client.create_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.create_case)
        """

    def describe_attachment(self, attachmentId: str) -> DescribeAttachmentResponseTypeDef:
        """
        [Client.describe_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_attachment)
        """

    def describe_cases(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        nextToken: str = None,
        maxResults: int = None,
        language: str = None,
        includeCommunications: bool = None,
    ) -> DescribeCasesResponseTypeDef:
        """
        [Client.describe_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_cases)
        """

    def describe_communications(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeCommunicationsResponseTypeDef:
        """
        [Client.describe_communications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_communications)
        """

    def describe_services(
        self, serviceCodeList: List[str] = None, language: str = None
    ) -> DescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_services)
        """

    def describe_severity_levels(
        self, language: str = None
    ) -> DescribeSeverityLevelsResponseTypeDef:
        """
        [Client.describe_severity_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_severity_levels)
        """

    def describe_trusted_advisor_check_refresh_statuses(
        self, checkIds: List[str]
    ) -> DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_refresh_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_trusted_advisor_check_refresh_statuses)
        """

    def describe_trusted_advisor_check_result(
        self, checkId: str, language: str = None
    ) -> DescribeTrustedAdvisorCheckResultResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_trusted_advisor_check_result)
        """

    def describe_trusted_advisor_check_summaries(
        self, checkIds: List[str]
    ) -> DescribeTrustedAdvisorCheckSummariesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_trusted_advisor_check_summaries)
        """

    def describe_trusted_advisor_checks(
        self, language: str
    ) -> DescribeTrustedAdvisorChecksResponseTypeDef:
        """
        [Client.describe_trusted_advisor_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.describe_trusted_advisor_checks)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.generate_presigned_url)
        """

    def refresh_trusted_advisor_check(
        self, checkId: str
    ) -> RefreshTrustedAdvisorCheckResponseTypeDef:
        """
        [Client.refresh_trusted_advisor_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.refresh_trusted_advisor_check)
        """

    def resolve_case(self, caseId: str = None) -> ResolveCaseResponseTypeDef:
        """
        [Client.resolve_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Client.resolve_case)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_cases"]) -> DescribeCasesPaginator:
        """
        [Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_communications"]
    ) -> DescribeCommunicationsPaginator:
        """
        [Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCommunications)
        """
