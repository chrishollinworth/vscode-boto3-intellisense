"""
Type annotations for support service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/paginators.html)

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

from .type_defs import (
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")

class DescribeCasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/support.html#Support.Paginator.DescribeCases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/paginators.html#describecasespaginator)
    """

    def paginate(
        self,
        *,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/support.html#Support.Paginator.DescribeCases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/paginators.html#describecasespaginator)
        """

class DescribeCommunicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/support.html#Support.Paginator.DescribeCommunications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/paginators.html#describecommunicationspaginator)
    """

    def paginate(
        self,
        *,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCommunicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/support.html#Support.Paginator.DescribeCommunications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/paginators.html#describecommunicationspaginator)
        """
