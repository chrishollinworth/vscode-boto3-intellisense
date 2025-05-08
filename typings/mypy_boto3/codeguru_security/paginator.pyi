"""
Type annotations for codeguru-security service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codeguru_security.client import CodeGuruSecurityClient
    from mypy_boto3_codeguru_security.paginator import (
        GetFindingsPaginator,
        ListFindingsMetricsPaginator,
        ListScansPaginator,
    )

    session = Session()
    client: CodeGuruSecurityClient = session.client("codeguru-security")

    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    list_findings_metrics_paginator: ListFindingsMetricsPaginator = client.get_paginator("list_findings_metrics")
    list_scans_paginator: ListScansPaginator = client.get_paginator("list_scans")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetFindingsRequestPaginateTypeDef,
    GetFindingsResponseTypeDef,
    ListFindingsMetricsRequestPaginateTypeDef,
    ListFindingsMetricsResponseTypeDef,
    ListScansRequestPaginateTypeDef,
    ListScansResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetFindingsPaginator", "ListFindingsMetricsPaginator", "ListScansPaginator")

if TYPE_CHECKING:
    _GetFindingsPaginatorBase = Paginator[GetFindingsResponseTypeDef]
else:
    _GetFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class GetFindingsPaginator(_GetFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/GetFindings.html#CodeGuruSecurity.Paginator.GetFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#getfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFindingsRequestPaginateTypeDef]
    ) -> PageIterator[GetFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/GetFindings.html#CodeGuruSecurity.Paginator.GetFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#getfindingspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsMetricsPaginatorBase = Paginator[ListFindingsMetricsResponseTypeDef]
else:
    _ListFindingsMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsMetricsPaginator(_ListFindingsMetricsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/ListFindingsMetrics.html#CodeGuruSecurity.Paginator.ListFindingsMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#listfindingsmetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsMetricsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/ListFindingsMetrics.html#CodeGuruSecurity.Paginator.ListFindingsMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#listfindingsmetricspaginator)
        """

if TYPE_CHECKING:
    _ListScansPaginatorBase = Paginator[ListScansResponseTypeDef]
else:
    _ListScansPaginatorBase = Paginator  # type: ignore[assignment]

class ListScansPaginator(_ListScansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/ListScans.html#CodeGuruSecurity.Paginator.ListScans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#listscanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScansRequestPaginateTypeDef]
    ) -> PageIterator[ListScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-security/paginator/ListScans.html#CodeGuruSecurity.Paginator.ListScans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/paginators/#listscanspaginator)
        """
