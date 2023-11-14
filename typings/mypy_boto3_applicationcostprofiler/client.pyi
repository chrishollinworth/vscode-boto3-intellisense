"""
Type annotations for applicationcostprofiler service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_applicationcostprofiler import ApplicationCostProfilerClient

    client: ApplicationCostProfilerClient = boto3.client("applicationcostprofiler")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import FormatType, ReportFrequencyType
from .paginator import ListReportDefinitionsPaginator
from .type_defs import (
    DeleteReportDefinitionResultTypeDef,
    GetReportDefinitionResultTypeDef,
    ImportApplicationUsageResultTypeDef,
    ListReportDefinitionsResultTypeDef,
    PutReportDefinitionResultTypeDef,
    S3LocationTypeDef,
    SourceS3LocationTypeDef,
    UpdateReportDefinitionResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ApplicationCostProfilerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ApplicationCostProfilerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationCostProfilerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#close)
        """
    def delete_report_definition(self, *, reportId: str) -> DeleteReportDefinitionResultTypeDef:
        """
        Deletes the specified report definition in AWS Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.delete_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#delete_report_definition)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#generate_presigned_url)
        """
    def get_report_definition(self, *, reportId: str) -> GetReportDefinitionResultTypeDef:
        """
        Retrieves the definition of a report already configured in AWS Application Cost
        Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.get_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#get_report_definition)
        """
    def import_application_usage(
        self, *, sourceS3Location: "SourceS3LocationTypeDef"
    ) -> ImportApplicationUsageResultTypeDef:
        """
        Ingests application usage data from Amazon Simple Storage Service (Amazon S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.import_application_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#import_application_usage)
        """
    def list_report_definitions(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListReportDefinitionsResultTypeDef:
        """
        Retrieves a list of all reports and their configurations for your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.list_report_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#list_report_definitions)
        """
    def put_report_definition(
        self,
        *,
        reportId: str,
        reportDescription: str,
        reportFrequency: ReportFrequencyType,
        format: FormatType,
        destinationS3Location: "S3LocationTypeDef"
    ) -> PutReportDefinitionResultTypeDef:
        """
        Creates the report definition for a report in Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.put_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#put_report_definition)
        """
    def update_report_definition(
        self,
        *,
        reportId: str,
        reportDescription: str,
        reportFrequency: ReportFrequencyType,
        format: FormatType,
        destinationS3Location: "S3LocationTypeDef"
    ) -> UpdateReportDefinitionResultTypeDef:
        """
        Updates existing report in AWS Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client.update_report_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client.html#update_report_definition)
        """
    def get_paginator(
        self, operation_name: Literal["list_report_definitions"]
    ) -> ListReportDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Paginator.ListReportDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/paginators.html#listreportdefinitionspaginator)
        """
