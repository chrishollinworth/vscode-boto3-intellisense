"""
Type annotations for artifact service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_artifact.client import ArtifactClient
    from mypy_boto3_artifact.paginator import (
        ListCustomerAgreementsPaginator,
        ListReportsPaginator,
    )

    session = Session()
    client: ArtifactClient = session.client("artifact")

    list_customer_agreements_paginator: ListCustomerAgreementsPaginator = client.get_paginator("list_customer_agreements")
    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCustomerAgreementsRequestPaginateTypeDef,
    ListCustomerAgreementsResponseTypeDef,
    ListReportsRequestPaginateTypeDef,
    ListReportsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListCustomerAgreementsPaginator", "ListReportsPaginator")

if TYPE_CHECKING:
    _ListCustomerAgreementsPaginatorBase = Paginator[ListCustomerAgreementsResponseTypeDef]
else:
    _ListCustomerAgreementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomerAgreementsPaginator(_ListCustomerAgreementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/artifact/paginator/ListCustomerAgreements.html#Artifact.Paginator.ListCustomerAgreements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators/#listcustomeragreementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomerAgreementsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomerAgreementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/artifact/paginator/ListCustomerAgreements.html#Artifact.Paginator.ListCustomerAgreements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators/#listcustomeragreementspaginator)
        """

if TYPE_CHECKING:
    _ListReportsPaginatorBase = Paginator[ListReportsResponseTypeDef]
else:
    _ListReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReportsPaginator(_ListReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/artifact/paginator/ListReports.html#Artifact.Paginator.ListReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators/#listreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReportsRequestPaginateTypeDef]
    ) -> PageIterator[ListReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/artifact/paginator/ListReports.html#Artifact.Paginator.ListReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/paginators/#listreportspaginator)
        """
