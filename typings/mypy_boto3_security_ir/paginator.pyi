"""
Type annotations for security-ir service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_security_ir.client import SecurityIncidentResponseClient
    from mypy_boto3_security_ir.paginator import (
        ListCaseEditsPaginator,
        ListCasesPaginator,
        ListCommentsPaginator,
        ListMembershipsPaginator,
    )

    session = Session()
    client: SecurityIncidentResponseClient = session.client("security-ir")

    list_case_edits_paginator: ListCaseEditsPaginator = client.get_paginator("list_case_edits")
    list_cases_paginator: ListCasesPaginator = client.get_paginator("list_cases")
    list_comments_paginator: ListCommentsPaginator = client.get_paginator("list_comments")
    list_memberships_paginator: ListMembershipsPaginator = client.get_paginator("list_memberships")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCaseEditsRequestPaginateTypeDef,
    ListCaseEditsResponseTypeDef,
    ListCasesRequestPaginateTypeDef,
    ListCasesResponseTypeDef,
    ListCommentsRequestPaginateTypeDef,
    ListCommentsResponseTypeDef,
    ListMembershipsRequestPaginateTypeDef,
    ListMembershipsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCaseEditsPaginator",
    "ListCasesPaginator",
    "ListCommentsPaginator",
    "ListMembershipsPaginator",
)

if TYPE_CHECKING:
    _ListCaseEditsPaginatorBase = Paginator[ListCaseEditsResponseTypeDef]
else:
    _ListCaseEditsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCaseEditsPaginator(_ListCaseEditsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListCaseEdits.html#SecurityIncidentResponse.Paginator.ListCaseEdits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcaseeditspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCaseEditsRequestPaginateTypeDef]
    ) -> PageIterator[ListCaseEditsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListCaseEdits.html#SecurityIncidentResponse.Paginator.ListCaseEdits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcaseeditspaginator)
        """

if TYPE_CHECKING:
    _ListCasesPaginatorBase = Paginator[ListCasesResponseTypeDef]
else:
    _ListCasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCasesPaginator(_ListCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListCases.html#SecurityIncidentResponse.Paginator.ListCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCasesRequestPaginateTypeDef]
    ) -> PageIterator[ListCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListCases.html#SecurityIncidentResponse.Paginator.ListCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcasespaginator)
        """

if TYPE_CHECKING:
    _ListCommentsPaginatorBase = Paginator[ListCommentsResponseTypeDef]
else:
    _ListCommentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCommentsPaginator(_ListCommentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListComments.html#SecurityIncidentResponse.Paginator.ListComments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcommentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCommentsRequestPaginateTypeDef]
    ) -> PageIterator[ListCommentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListComments.html#SecurityIncidentResponse.Paginator.ListComments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listcommentspaginator)
        """

if TYPE_CHECKING:
    _ListMembershipsPaginatorBase = Paginator[ListMembershipsResponseTypeDef]
else:
    _ListMembershipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMembershipsPaginator(_ListMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListMemberships.html#SecurityIncidentResponse.Paginator.ListMemberships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listmembershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMembershipsRequestPaginateTypeDef]
    ) -> PageIterator[ListMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/paginator/ListMemberships.html#SecurityIncidentResponse.Paginator.ListMemberships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/paginators/#listmembershipspaginator)
        """
