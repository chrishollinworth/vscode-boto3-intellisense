"""
Type annotations for emr-serverless service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_emr_serverless.client import EMRServerlessClient
    from mypy_boto3_emr_serverless.paginator import (
        ListApplicationsPaginator,
        ListJobRunAttemptsPaginator,
        ListJobRunsPaginator,
    )

    session = Session()
    client: EMRServerlessClient = session.client("emr-serverless")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_run_attempts_paginator: ListJobRunAttemptsPaginator = client.get_paginator("list_job_run_attempts")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListJobRunAttemptsRequestPaginateTypeDef,
    ListJobRunAttemptsResponseTypeDef,
    ListJobRunsRequestPaginateTypeDef,
    ListJobRunsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListApplicationsPaginator", "ListJobRunAttemptsPaginator", "ListJobRunsPaginator")

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListApplications.html#EMRServerless.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListApplications.html#EMRServerless.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListJobRunAttemptsPaginatorBase = Paginator[ListJobRunAttemptsResponseTypeDef]
else:
    _ListJobRunAttemptsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobRunAttemptsPaginator(_ListJobRunAttemptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListJobRunAttempts.html#EMRServerless.Paginator.ListJobRunAttempts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunattemptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobRunAttemptsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobRunAttemptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListJobRunAttempts.html#EMRServerless.Paginator.ListJobRunAttempts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunattemptspaginator)
        """

if TYPE_CHECKING:
    _ListJobRunsPaginatorBase = Paginator[ListJobRunsResponseTypeDef]
else:
    _ListJobRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobRunsPaginator(_ListJobRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListJobRuns.html#EMRServerless.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/paginator/ListJobRuns.html#EMRServerless.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators/#listjobrunspaginator)
        """
