"""
Type annotations for emr-serverless service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_emr_serverless import EMRServerlessClient
    from mypy_boto3_emr_serverless.paginator import (
        ListApplicationsPaginator,
        ListJobRunAttemptsPaginator,
        ListJobRunsPaginator,
    )

    client: EMRServerlessClient = boto3.client("emr-serverless")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_run_attempts_paginator: ListJobRunAttemptsPaginator = client.get_paginator("list_job_run_attempts")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ApplicationStateType, JobRunModeType, JobRunStateType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListJobRunAttemptsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListApplicationsPaginator", "ListJobRunAttemptsPaginator", "ListJobRunsPaginator")

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        states: List[ApplicationStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listapplicationspaginator)
        """

class ListJobRunAttemptsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRunAttempts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunattemptspaginator)
    """

    def paginate(
        self, *, applicationId: str, jobRunId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunAttemptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRunAttempts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunattemptspaginator)
        """

class ListJobRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        createdAtAfter: Union[datetime, str] = None,
        createdAtBefore: Union[datetime, str] = None,
        states: List[JobRunStateType] = None,
        mode: JobRunModeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunspaginator)
        """
