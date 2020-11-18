# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for support service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_support import SupportClient
    from mypy_boto3_support.paginator import (
        DescribeCasesPaginator,
        DescribeCommunicationsPaginator,
    )

    client: SupportClient = boto3.client("support")

    describe_cases_paginator: DescribeCasesPaginator = client.get_paginator("describe_cases")
    describe_communications_paginator: DescribeCommunicationsPaginator = client.get_paginator("describe_communications")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_support.type_defs import (
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")


class DescribeCasesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCases)
    """

    def paginate(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCasesResponseTypeDef]:
        """
        [DescribeCases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCases.paginate)
        """


class DescribeCommunicationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCommunications)
    """

    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCommunicationsResponseTypeDef]:
        """
        [DescribeCommunications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/support.html#Support.Paginator.DescribeCommunications.paginate)
        """
