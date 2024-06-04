"""
Type annotations for artifact service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_artifact import ArtifactClient
    from mypy_boto3_artifact.paginator import (
        ListReportsPaginator,
    )

    client: ArtifactClient = boto3.client("artifact")

    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListReportsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListReportsPaginator",)

class ListReportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Paginator.ListReports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators.html#listreportspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/artifact.html#Artifact.Paginator.ListReports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators.html#listreportspaginator)
        """
