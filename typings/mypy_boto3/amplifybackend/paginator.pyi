"""
Type annotations for amplifybackend service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amplifybackend import AmplifyBackendClient
    from mypy_boto3_amplifybackend.paginator import (
        ListBackendJobsPaginator,
    )

    client: AmplifyBackendClient = boto3.client("amplifybackend")

    list_backend_jobs_paginator: ListBackendJobsPaginator = client.get_paginator("list_backend_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListBackendJobsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListBackendJobsPaginator",)

class ListBackendJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/amplifybackend.html#AmplifyBackend.Paginator.ListBackendJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators.html#listbackendjobspaginator)
    """

    def paginate(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str = None,
        Operation: str = None,
        Status: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackendJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/amplifybackend.html#AmplifyBackend.Paginator.ListBackendJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators.html#listbackendjobspaginator)
        """
