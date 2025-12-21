"""
Type annotations for mpa service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mpa.client import MultipartyApprovalClient
    from mypy_boto3_mpa.paginator import (
        ListApprovalTeamsPaginator,
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyVersionsPaginator,
        ListResourcePoliciesPaginator,
        ListSessionsPaginator,
    )

    session = Session()
    client: MultipartyApprovalClient = session.client("mpa")

    list_approval_teams_paginator: ListApprovalTeamsPaginator = client.get_paginator("list_approval_teams")
    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_versions_paginator: ListPolicyVersionsPaginator = client.get_paginator("list_policy_versions")
    list_resource_policies_paginator: ListResourcePoliciesPaginator = client.get_paginator("list_resource_policies")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApprovalTeamsRequestPaginateTypeDef,
    ListApprovalTeamsResponseTypeDef,
    ListIdentitySourcesRequestPaginateTypeDef,
    ListIdentitySourcesResponseTypeDef,
    ListPoliciesRequestPaginateTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyVersionsRequestPaginateTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListResourcePoliciesRequestPaginateTypeDef,
    ListResourcePoliciesResponseTypeDef,
    ListSessionsRequestPaginateTypeDef,
    ListSessionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApprovalTeamsPaginator",
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyVersionsPaginator",
    "ListResourcePoliciesPaginator",
    "ListSessionsPaginator",
)

if TYPE_CHECKING:
    _ListApprovalTeamsPaginatorBase = Paginator[ListApprovalTeamsResponseTypeDef]
else:
    _ListApprovalTeamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApprovalTeamsPaginator(_ListApprovalTeamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListApprovalTeams.html#MultipartyApproval.Paginator.ListApprovalTeams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listapprovalteamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApprovalTeamsRequestPaginateTypeDef]
    ) -> PageIterator[ListApprovalTeamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListApprovalTeams.html#MultipartyApproval.Paginator.ListApprovalTeams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listapprovalteamspaginator)
        """

if TYPE_CHECKING:
    _ListIdentitySourcesPaginatorBase = Paginator[ListIdentitySourcesResponseTypeDef]
else:
    _ListIdentitySourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentitySourcesPaginator(_ListIdentitySourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListIdentitySources.html#MultipartyApproval.Paginator.ListIdentitySources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listidentitysourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentitySourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListIdentitySourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListIdentitySources.html#MultipartyApproval.Paginator.ListIdentitySources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listidentitysourcespaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesResponseTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListPolicies.html#MultipartyApproval.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListPolicies.html#MultipartyApproval.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyVersionsPaginatorBase = Paginator[ListPolicyVersionsResponseTypeDef]
else:
    _ListPolicyVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyVersionsPaginator(_ListPolicyVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListPolicyVersions.html#MultipartyApproval.Paginator.ListPolicyVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listpolicyversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListPolicyVersions.html#MultipartyApproval.Paginator.ListPolicyVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listpolicyversionspaginator)
        """

if TYPE_CHECKING:
    _ListResourcePoliciesPaginatorBase = Paginator[ListResourcePoliciesResponseTypeDef]
else:
    _ListResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcePoliciesPaginator(_ListResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListResourcePolicies.html#MultipartyApproval.Paginator.ListResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListResourcePolicies.html#MultipartyApproval.Paginator.ListResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsResponseTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListSessions.html#MultipartyApproval.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/paginator/ListSessions.html#MultipartyApproval.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/paginators/#listsessionspaginator)
        """
