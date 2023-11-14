"""
Type annotations for codeguru-security service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_codeguru_security import CodeGuruSecurityClient
    from mypy_boto3_codeguru_security.paginator import (
        GetFindingsPaginator,
        ListFindingsMetricsPaginator,
        ListScansPaginator,
    )

    client: CodeGuruSecurityClient = boto3.client("codeguru-security")

    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    list_findings_metrics_paginator: ListFindingsMetricsPaginator = client.get_paginator("list_findings_metrics")
    list_scans_paginator: ListScansPaginator = client.get_paginator("list_scans")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import StatusType
from .type_defs import (
    GetFindingsResponseTypeDef,
    ListFindingsMetricsResponseTypeDef,
    ListScansResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("GetFindingsPaginator", "ListFindingsMetricsPaginator", "ListScansPaginator")

class GetFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.GetFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#getfindingspaginator)
    """

    def paginate(
        self,
        *,
        scanName: str,
        status: StatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.GetFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#getfindingspaginator)
        """

class ListFindingsMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListFindingsMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listfindingsmetricspaginator)
    """

    def paginate(
        self,
        *,
        endDate: Union[datetime, str],
        startDate: Union[datetime, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFindingsMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListFindingsMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listfindingsmetricspaginator)
        """

class ListScansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListScans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listscanspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/codeguru-security.html#CodeGuruSecurity.Paginator.ListScans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators.html#listscanspaginator)
        """
