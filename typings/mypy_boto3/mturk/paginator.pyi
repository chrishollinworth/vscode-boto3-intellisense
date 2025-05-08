"""
Type annotations for mturk service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mturk.client import MTurkClient
    from mypy_boto3_mturk.paginator import (
        ListAssignmentsForHITPaginator,
        ListBonusPaymentsPaginator,
        ListHITsForQualificationTypePaginator,
        ListHITsPaginator,
        ListQualificationRequestsPaginator,
        ListQualificationTypesPaginator,
        ListReviewableHITsPaginator,
        ListWorkerBlocksPaginator,
        ListWorkersWithQualificationTypePaginator,
    )

    session = Session()
    client: MTurkClient = session.client("mturk")

    list_assignments_for_hit_paginator: ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
    list_bonus_payments_paginator: ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
    list_hits_for_qualification_type_paginator: ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
    list_hits_paginator: ListHITsPaginator = client.get_paginator("list_hits")
    list_qualification_requests_paginator: ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
    list_qualification_types_paginator: ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
    list_reviewable_hits_paginator: ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
    list_worker_blocks_paginator: ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
    list_workers_with_qualification_type_paginator: ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssignmentsForHITRequestPaginateTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsRequestPaginateTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeRequestPaginateTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsRequestPaginateTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsRequestPaginateTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesRequestPaginateTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsRequestPaginateTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListWorkerBlocksRequestPaginateTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeRequestPaginateTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListHITsPaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)

if TYPE_CHECKING:
    _ListAssignmentsForHITPaginatorBase = Paginator[ListAssignmentsForHITResponseTypeDef]
else:
    _ListAssignmentsForHITPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssignmentsForHITPaginator(_ListAssignmentsForHITPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListAssignmentsForHIT.html#MTurk.Paginator.ListAssignmentsForHIT)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listassignmentsforhitpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssignmentsForHITRequestPaginateTypeDef]
    ) -> PageIterator[ListAssignmentsForHITResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListAssignmentsForHIT.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listassignmentsforhitpaginator)
        """

if TYPE_CHECKING:
    _ListBonusPaymentsPaginatorBase = Paginator[ListBonusPaymentsResponseTypeDef]
else:
    _ListBonusPaymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBonusPaymentsPaginator(_ListBonusPaymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListBonusPayments.html#MTurk.Paginator.ListBonusPayments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listbonuspaymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBonusPaymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListBonusPaymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListBonusPayments.html#MTurk.Paginator.ListBonusPayments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listbonuspaymentspaginator)
        """

if TYPE_CHECKING:
    _ListHITsForQualificationTypePaginatorBase = Paginator[
        ListHITsForQualificationTypeResponseTypeDef
    ]
else:
    _ListHITsForQualificationTypePaginatorBase = Paginator  # type: ignore[assignment]

class ListHITsForQualificationTypePaginator(_ListHITsForQualificationTypePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListHITsForQualificationType.html#MTurk.Paginator.ListHITsForQualificationType)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitsforqualificationtypepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHITsForQualificationTypeRequestPaginateTypeDef]
    ) -> PageIterator[ListHITsForQualificationTypeResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListHITsForQualificationType.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitsforqualificationtypepaginator)
        """

if TYPE_CHECKING:
    _ListHITsPaginatorBase = Paginator[ListHITsResponseTypeDef]
else:
    _ListHITsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHITsPaginator(_ListHITsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListHITs.html#MTurk.Paginator.ListHITs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHITsRequestPaginateTypeDef]
    ) -> PageIterator[ListHITsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListHITs.html#MTurk.Paginator.ListHITs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitspaginator)
        """

if TYPE_CHECKING:
    _ListQualificationRequestsPaginatorBase = Paginator[ListQualificationRequestsResponseTypeDef]
else:
    _ListQualificationRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQualificationRequestsPaginator(_ListQualificationRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListQualificationRequests.html#MTurk.Paginator.ListQualificationRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationrequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQualificationRequestsRequestPaginateTypeDef]
    ) -> PageIterator[ListQualificationRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListQualificationRequests.html#MTurk.Paginator.ListQualificationRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationrequestspaginator)
        """

if TYPE_CHECKING:
    _ListQualificationTypesPaginatorBase = Paginator[ListQualificationTypesResponseTypeDef]
else:
    _ListQualificationTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQualificationTypesPaginator(_ListQualificationTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListQualificationTypes.html#MTurk.Paginator.ListQualificationTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQualificationTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListQualificationTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListQualificationTypes.html#MTurk.Paginator.ListQualificationTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationtypespaginator)
        """

if TYPE_CHECKING:
    _ListReviewableHITsPaginatorBase = Paginator[ListReviewableHITsResponseTypeDef]
else:
    _ListReviewableHITsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReviewableHITsPaginator(_ListReviewableHITsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListReviewableHITs.html#MTurk.Paginator.ListReviewableHITs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listreviewablehitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReviewableHITsRequestPaginateTypeDef]
    ) -> PageIterator[ListReviewableHITsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListReviewableHITs.html#MTurk.Paginator.ListReviewableHITs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listreviewablehitspaginator)
        """

if TYPE_CHECKING:
    _ListWorkerBlocksPaginatorBase = Paginator[ListWorkerBlocksResponseTypeDef]
else:
    _ListWorkerBlocksPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkerBlocksPaginator(_ListWorkerBlocksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListWorkerBlocks.html#MTurk.Paginator.ListWorkerBlocks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerblockspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkerBlocksRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkerBlocksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListWorkerBlocks.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerblockspaginator)
        """

if TYPE_CHECKING:
    _ListWorkersWithQualificationTypePaginatorBase = Paginator[
        ListWorkersWithQualificationTypeResponseTypeDef
    ]
else:
    _ListWorkersWithQualificationTypePaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkersWithQualificationTypePaginator(_ListWorkersWithQualificationTypePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListWorkersWithQualificationType.html#MTurk.Paginator.ListWorkersWithQualificationType)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerswithqualificationtypepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkersWithQualificationTypeRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkersWithQualificationTypeResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk/paginator/ListWorkersWithQualificationType.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerswithqualificationtypepaginator)
        """
