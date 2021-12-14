"""
Type annotations for cur service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cur import CostandUsageReportServiceClient

    client: CostandUsageReportServiceClient = boto3.client("cur")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import DescribeReportDefinitionsPaginator
from .type_defs import (
    DeleteReportDefinitionResponseTypeDef,
    DescribeReportDefinitionsResponseTypeDef,
    ReportDefinitionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CostandUsageReportServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DuplicateReportNameException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    ReportLimitReachedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CostandUsageReportServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CostandUsageReportServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#can_paginate)
        """
    def delete_report_definition(
        self, *, ReportName: str = None
    ) -> DeleteReportDefinitionResponseTypeDef:
        """
        Deletes the specified report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.delete_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#delete_report_definition)
        """
    def describe_report_definitions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeReportDefinitionsResponseTypeDef:
        """
        Lists the AWS Cost and Usage reports available to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.describe_report_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#describe_report_definitions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#generate_presigned_url)
        """
    def modify_report_definition(
        self, *, ReportName: str, ReportDefinition: "ReportDefinitionTypeDef"
    ) -> Dict[str, Any]:
        """
        Allows you to programatically update your report preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.modify_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#modify_report_definition)
        """
    def put_report_definition(
        self, *, ReportDefinition: "ReportDefinitionTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates a new report using the description that you provide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Client.put_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/client.html#put_report_definition)
        """
    def get_paginator(
        self, operation_name: Literal["describe_report_definitions"]
    ) -> DescribeReportDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/paginators.html#describereportdefinitionspaginator)
        """
