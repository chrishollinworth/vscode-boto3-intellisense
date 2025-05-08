"""
Type annotations for applicationcostprofiler service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_applicationcostprofiler.client import ApplicationCostProfilerClient

    session = Session()
    client: ApplicationCostProfilerClient = session.client("applicationcostprofiler")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListReportDefinitionsPaginator
from .type_defs import (
    DeleteReportDefinitionRequestTypeDef,
    DeleteReportDefinitionResultTypeDef,
    GetReportDefinitionRequestTypeDef,
    GetReportDefinitionResultTypeDef,
    ImportApplicationUsageRequestTypeDef,
    ImportApplicationUsageResultTypeDef,
    ListReportDefinitionsRequestTypeDef,
    ListReportDefinitionsResultTypeDef,
    PutReportDefinitionRequestTypeDef,
    PutReportDefinitionResultTypeDef,
    UpdateReportDefinitionRequestTypeDef,
    UpdateReportDefinitionResultTypeDef,
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

__all__ = ("ApplicationCostProfilerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ApplicationCostProfilerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationCostProfilerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler.html#ApplicationCostProfiler.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#generate_presigned_url)
        """

    def delete_report_definition(
        self, **kwargs: Unpack[DeleteReportDefinitionRequestTypeDef]
    ) -> DeleteReportDefinitionResultTypeDef:
        """
        Deletes the specified report definition in AWS Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/delete_report_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#delete_report_definition)
        """

    def get_report_definition(
        self, **kwargs: Unpack[GetReportDefinitionRequestTypeDef]
    ) -> GetReportDefinitionResultTypeDef:
        """
        Retrieves the definition of a report already configured in AWS Application Cost
        Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/get_report_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#get_report_definition)
        """

    def import_application_usage(
        self, **kwargs: Unpack[ImportApplicationUsageRequestTypeDef]
    ) -> ImportApplicationUsageResultTypeDef:
        """
        Ingests application usage data from Amazon Simple Storage Service (Amazon S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/import_application_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#import_application_usage)
        """

    def list_report_definitions(
        self, **kwargs: Unpack[ListReportDefinitionsRequestTypeDef]
    ) -> ListReportDefinitionsResultTypeDef:
        """
        Retrieves a list of all reports and their configurations for your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/list_report_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#list_report_definitions)
        """

    def put_report_definition(
        self, **kwargs: Unpack[PutReportDefinitionRequestTypeDef]
    ) -> PutReportDefinitionResultTypeDef:
        """
        Creates the report definition for a report in Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/put_report_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#put_report_definition)
        """

    def update_report_definition(
        self, **kwargs: Unpack[UpdateReportDefinitionRequestTypeDef]
    ) -> UpdateReportDefinitionResultTypeDef:
        """
        Updates existing report in AWS Application Cost Profiler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/update_report_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#update_report_definition)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_report_definitions"]
    ) -> ListReportDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/client/#get_paginator)
        """
