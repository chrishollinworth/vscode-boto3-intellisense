"""
Type annotations for emr-serverless service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_emr_serverless import EMRServerlessClient
    from mypy_boto3_emr_serverless.paginator import (
        ListApplicationsPaginator,
        ListJobRunsPaginator,
    )

    client: EMRServerlessClient = boto3.client("emr-serverless")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ApplicationStateType, JobRunStateType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListApplicationsPaginator", "ListJobRunsPaginator")

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        states: List[ApplicationStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listapplicationspaginator)
        """

class ListJobRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        createdAtAfter: Union[datetime, str] = None,
        createdAtBefore: Union[datetime, str] = None,
        states: List[JobRunStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunspaginator)
        """
