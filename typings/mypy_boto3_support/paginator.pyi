"""
Type annotations for support service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_support.client import SupportClient
    from mypy_boto3_support.paginator import (
        DescribeCasesPaginator,
        DescribeCommunicationsPaginator,
    )

    session = Session()
    client: SupportClient = session.client("support")

    describe_cases_paginator: DescribeCasesPaginator = client.get_paginator("describe_cases")
    describe_communications_paginator: DescribeCommunicationsPaginator = client.get_paginator("describe_communications")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeCasesRequestPaginateTypeDef,
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsRequestPaginateTypeDef,
    DescribeCommunicationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")

if TYPE_CHECKING:
    _DescribeCasesPaginatorBase = Paginator[DescribeCasesResponseTypeDef]
else:
    _DescribeCasesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCasesPaginator(_DescribeCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/paginator/DescribeCases.html#Support.Paginator.DescribeCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/paginators/#describecasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCasesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/paginator/DescribeCases.html#Support.Paginator.DescribeCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/paginators/#describecasespaginator)
        """

if TYPE_CHECKING:
    _DescribeCommunicationsPaginatorBase = Paginator[DescribeCommunicationsResponseTypeDef]
else:
    _DescribeCommunicationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCommunicationsPaginator(_DescribeCommunicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/paginator/DescribeCommunications.html#Support.Paginator.DescribeCommunications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/paginators/#describecommunicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCommunicationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCommunicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support/paginator/DescribeCommunications.html#Support.Paginator.DescribeCommunications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/paginators/#describecommunicationspaginator)
        """
